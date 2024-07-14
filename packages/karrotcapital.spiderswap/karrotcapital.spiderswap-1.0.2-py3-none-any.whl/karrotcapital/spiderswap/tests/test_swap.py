import pytest
import asyncio
import base64
from solana.transaction import Transaction, TransactionError, Keypair
from solana.rpc.core import Blockhash
from karrotcapital.spiderswap import Spiderswap
from unittest.mock import AsyncMock, MagicMock
from solders.message import MessageV0
from solders.transaction import VersionedTransaction

@pytest.fixture
def spiderswap():
    api_key = '8fd8b157e86f072b5cfaa7df4740985b'
    return Spiderswap(api_key)

@pytest.mark.asyncio
async def test_get_swap_raw(spiderswap):
    from aiohttp import ClientSession

    owner = 'Etm8Fq3BLSNcR8hLN1zpDoUALQJLJyspVTxPNVbx66Ec'
    from_mint = 'So11111111111111111111111111111111111111112'
    to_mint = 'AT79ReYU9XtHUTF5vM6Q4oa9K8w7918Fp5SU7G1MDMQY'
    amount = 1000000  # in lamports
    slippage = 50  # in bps
    provider = 'raydium'
    pool = None

    # Mock the aiohttp session and response
    async def mock_get(*args, **kwargs):
        class MockResponse:
            status = 200

            async def json(self):
                return {
                    'data': {
                        'base64Transaction': 'dGVzdA==',  # example base64 encoded string
                        'signers': ['signer1', 'signer2']
                    }
                }

            async def __aenter__(self):
                return self

            async def __aexit__(self, exc_type, exc, tb):
                pass

        return MockResponse()

    async with ClientSession() as session:
        spiderswap.swap.get_swap_raw.__globals__['aiohttp'].ClientSession().get = mock_get

        result = await spiderswap.swap.get_swap_raw(owner, from_mint, to_mint, amount, slippage, provider, pool)

        assert isinstance(result['base64Transaction'], str)
        assert result['signers'] == []

@pytest.mark.asyncio
async def test_get_swap(spiderswap):
    from aiohttp import ClientSession

    owner = 'Etm8Fq3BLSNcR8hLN1zpDoUALQJLJyspVTxPNVbx66Ec'
    from_mint = 'So11111111111111111111111111111111111111112'
    to_mint = 'AT79ReYU9XtHUTF5vM6Q4oa9K8w7918Fp5SU7G1MDMQY'
    amount = 1.0  # in tokens
    slippage = 0.5  # in percentage
    provider = 'raydium'
    pool = None
    from_mint_decimals = 9

    # Mock the get_swap_raw method
    async def mock_get_swap_raw(owner, from_mint, to_mint, new_amount, slippage, provider, pool):
        return {
            'base64Transaction': 'dGVzdA==',  # example base64 encoded string
            'signers': ['signer1', 'signer2']
        }

    async with ClientSession() as session:
        spiderswap.swap.get_swap_raw = mock_get_swap_raw

        result = await spiderswap.swap.get_swap(owner, from_mint, to_mint, amount, slippage, provider, pool, from_mint_decimals)

        assert result['base64Transaction'] == 'dGVzdA=='
        assert result['signers'] == ['signer1', 'signer2']

@pytest.mark.asyncio
async def test_create_transaction(mocker, spiderswap):
    swap_transaction_data = 'dGVzdA=='  # example base64 encoded string
    swap_transaction_buf = base64.b64decode(swap_transaction_data)

    # Mock the Transaction.deserialize method
    mock_transaction_class = mocker.patch('solders.transaction.VersionedTransaction')
    mock_transaction_instance = MagicMock()
    mock_transaction_instance.message = MagicMock()
    mock_transaction_class.deserialize.return_value = mock_transaction_instance

    result = await spiderswap.swap.create_transaction(swap_transaction_data)

    # Verify the call to deserialize
    mock_transaction_class.deserialize.assert_called_once_with(swap_transaction_buf)

    # Update this assertion based on what create_transaction should return
    assert result == 'deserialized transaction'

@pytest.fixture
def mock_keypair(mocker):
    mock_keypair = mocker.patch('solana.transaction.Keypair')
    mock_keypair_instance = MagicMock()
    mock_keypair.from_base58_string.return_value = mock_keypair_instance
    return mock_keypair, mock_keypair_instance

@pytest.fixture
def mock_connection(mocker):
    mock_connection_class = mocker.patch('solana.rpc.async_api.AsyncClient')
    mock_connection_instance = AsyncMock()
    mock_connection_class.return_value = mock_connection_instance
    return mock_connection_instance

@pytest.fixture
def mock_transaction():
    mock_transaction = MagicMock(spec=VersionedTransaction)
    mock_message = MagicMock(spec=MessageV0)
    mock_transaction.message = mock_message
    return mock_transaction, mock_message

@pytest.mark.asyncio
async def test_send_transaction_success(mock_keypair, mock_connection, mock_transaction):
    mock_keypair_class, mock_keypair_instance = mock_keypair
    mock_connection_instance = mock_connection
    mock_transaction, mock_message = mock_transaction

    mock_connection_instance.get_latest_blockhash.return_value = AsyncMock(value=MagicMock(blockhash='dummy_blockhash', last_valid_block_height=100))
    mock_connection_instance.send_raw_transaction.return_value = AsyncMock(value='dummy_signature')
    mock_connection_instance.confirm_transaction.return_value = AsyncMock(value=[MagicMock(err=None)])

    # Create an instance of MyClass (replace with the actual class name)
    my_instance = spiderswap()
    
    # Call the function
    result = await my_instance.swap.send_transaction(
        rpc_endpoint='http://dummy_rpc_endpoint',
        transaction=mock_transaction,
        private_key='dummy_private_key'
    )
    
    # Assertions
    assert result == 'dummy_signature'
    mock_connection_instance.get_latest_blockhash.assert_called_once_with('confirmed')
    mock_connection_instance.send_raw_transaction.assert_called_once()
    mock_connection_instance.confirm_transaction.assert_called_once_with('dummy_signature', commitment='confirmed')

@pytest.mark.asyncio
async def test_send_transaction_retry_on_expired(mock_keypair, mock_connection, mock_transaction):
    mock_keypair_class, mock_keypair_instance = mock_keypair
    mock_connection_instance = mock_connection
    mock_transaction, mock_message = mock_transaction

    mock_connection_instance.get_latest_blockhash.return_value = AsyncMock(value=MagicMock(blockhash='dummy_blockhash', last_valid_block_height=100))
    mock_connection_instance.send_raw_transaction.side_effect = [AsyncMock(value='expired_signature'), AsyncMock(value='dummy_signature')]
    mock_connection_instance.confirm_transaction.side_effect = [AsyncMock(value=[MagicMock(err='TransactionExpired')]), AsyncMock(value=[MagicMock(err=None)])]

    # Create an instance of MyClass (replace with the actual class name)
    my_instance = spiderswap()
    
    # Call the function
    result = await my_instance.swap.send_transaction(
        rpc_endpoint='http://dummy_rpc_endpoint',
        transaction=mock_transaction,
        private_key='dummy_private_key'
    )
    
    # Assertions
    assert result == 'dummy_signature'
    assert mock_connection_instance.send_raw_transaction.call_count == 2
    assert mock_connection_instance.confirm_transaction.call_count == 2

@pytest.mark.asyncio
async def test_send_transaction_failure(mock_keypair, mock_connection, mock_transaction):
    mock_keypair_class, mock_keypair_instance = mock_keypair
    mock_connection_instance = mock_connection
    mock_transaction, mock_message = mock_transaction

    mock_connection_instance.get_latest_blockhash.return_value = AsyncMock(value=MagicMock(blockhash='dummy_blockhash', last_valid_block_height=100))
    mock_connection_instance.send_raw_transaction.side_effect = AsyncMock(value='dummy_signature')
    mock_connection_instance.confirm_transaction.side_effect = [AsyncMock(value=[MagicMock(err='SomeError')])] * 3

    # Create an instance of MyClass (replace with the actual class name)
    my_instance = spiderswap()
    
    # Assertions for the raised exception
    with pytest.raises(Exception, match='Failed to send transaction after multiple attempts'):
        await my_instance.swap.send_transaction(
            rpc_endpoint='http://dummy_rpc_endpoint',
            transaction=mock_transaction,
            private_key='dummy_private_key'
        )
    assert mock_connection_instance.send_raw_transaction.call_count == 3
    assert mock_connection_instance.confirm_transaction.call_count == 3
