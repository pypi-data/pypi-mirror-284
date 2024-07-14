import aiohttp
import base64
from typing import List, Optional, TypedDict
from solana.transaction import Keypair
from solana.rpc.async_api import AsyncClient as Connection
from solana.rpc.commitment import Confirmed
from solana.rpc.types import TxOpts
from solana.rpc.core import RPCException
import base58
import math
from solders.message import MessageV0
from solders.transaction import VersionedTransaction

class SwapResponse(TypedDict):
    base64Transaction: str
    signers: List[str]

class Swap:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    async def get_swap_raw(self, owner: str, from_mint: str, to_mint: str, amount: int, slippage: int, provider: str, pool: Optional[str] = None) -> SwapResponse:
        body = {
            'owner': owner,
            'fromMint': from_mint,
            'toMint': to_mint,
            'amount': math.ceil(amount),
            'slippage': math.ceil(slippage),
            'provider': provider
        }

        if pool:
            body['pool'] = pool

        headers = {
            'X-API-KEY': self.api_key
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.base_url}/swap', params=body, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['data']
                else:
                    error_message = await response.text()
                    print(f'Error fetching swap data: {error_message}')
                    raise Exception('Failed to fetch swap data')

    async def get_swap(self, owner: str, from_mint: str, to_mint: str, amount: float, slippage: float, provider: str, pool: Optional[str] = None, from_mint_decimals: int = 9) -> SwapResponse:
        amount = amount * 10**from_mint_decimals  # convert to lamports
        slippage = slippage * 100  # convert to bps

        return await self.get_swap_raw(owner, from_mint, to_mint, int(amount), int(slippage), provider, pool)

    async def create_transaction(self, swap_transaction_data: str) -> VersionedTransaction:
        swap_transaction_buf = base64.b64decode(swap_transaction_data)
        return VersionedTransaction.from_bytes(swap_transaction_buf)

    
    async def send_transaction(self, rpc_endpoint: str, transaction: VersionedTransaction, private_key: str, additional_signers: Optional[List[str]] = None, retries: int = 3) -> str:
        connection = Connection(rpc_endpoint)
        keypair = Keypair.from_base58_string(private_key)

        # Convert additional signers to Keypair objects
        signers: List[Keypair] = []
        if additional_signers is not None:
            signers = [Keypair.from_base58_string(signer_key) for signer_key in additional_signers]

        for attempt in range(retries):
            try:
                # Fetch the latest blockhash and last valid block height
                latest_blockhash_resp = await connection.get_latest_blockhash('confirmed')
                blockhash = latest_blockhash_resp.value.blockhash
                last_valid_block_height = latest_blockhash_resp.value.last_valid_block_height

                # Extract the message from the versioned transaction
                original_message = transaction.message
                if not isinstance(original_message, MessageV0):
                    raise TypeError("Expected MessageV0 in VersionedTransaction")
                
                # Create a new MessageV0 with the updated blockhash
                message = MessageV0(
                    header=original_message.header,
                    account_keys=original_message.account_keys,
                    recent_blockhash=blockhash,
                    instructions=original_message.instructions,
                    address_table_lookups=original_message.address_table_lookups,
                )
                
                # Create a new VersionedTransaction with the updated message
                new_transaction = VersionedTransaction(message, [keypair, *signers])

                # Serialize the transaction
                serialized_transaction = bytes(new_transaction)

                signature = await connection.send_raw_transaction(serialized_transaction, opts=TxOpts(skip_preflight=False, preflight_commitment='confirmed'))

                # Confirm the transaction using the new method
                confirmation = await connection.confirm_transaction(signature.value, commitment='confirmed')
                
                if confirmation.value[0].err:
                    raise RPCException(confirmation.value[0].err)

                return signature.value
            except RPCException as error:
                if 'TransactionExpired' in str(error) and attempt < retries - 1:
                    print(f'Transaction expired, retrying... Attempt: {attempt + 1}')
                    continue
                print("Error sending transaction:", error)
                print("Transaction logs:", error.logs if hasattr(error, 'logs') else "No logs available")
                raise
            except Exception as error:
                print("Error sending transaction:", error)
                raise

        raise Exception('Failed to send transaction after multiple attempts')