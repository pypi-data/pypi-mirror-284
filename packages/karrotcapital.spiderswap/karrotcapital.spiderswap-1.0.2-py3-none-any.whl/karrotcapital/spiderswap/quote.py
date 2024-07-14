import aiohttp
import asyncio
import math
from typing import TypedDict, List, Any

class QuoteMap(TypedDict):
    inputMint: str
    inAmount: Any
    outputMint: str
    outAmount: Any
    minimumReceived: Any
    slippage: int
    priceImpactPercent: Any

class QuoteResponseMap(TypedDict):
    inputMint: str
    inAmount: float
    outputMint: str
    outAmount: float
    minimumReceived: float
    slippage: float
    priceImpactPercent: float

class BulkQuoteResponseMap(TypedDict):
    provider: str
    quote: QuoteResponseMap

class Quote:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    async def get_quote_raw(self, from_mint: str, to_mint: str, amount: float, slippage: float, provider: str) -> QuoteMap:
        params = {
            'fromMint': from_mint,
            'toMint': to_mint,
            'amount': math.ceil(amount),
            'slippage': math.ceil(slippage),
            'provider': provider
        }

        headers = {
            'X-API-KEY': self.api_key
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.base_url}/quote', params=params, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['data']
                else:
                    error_message = await response.text()
                    print(f'Error fetching quote data: {error_message}')
                    raise Exception('Failed to fetch quote data')

    async def get_quote(self, from_mint: str, to_mint: str, amount: float, slippage: float, provider: str, from_mint_decimals: int = 9, to_mint_decimals: int = 9) -> QuoteResponseMap:
        new_amount = amount * 10**from_mint_decimals  # convert to lamports
        slippage = slippage * 100  # convert to bps

        quote_response = await self.get_quote_raw(from_mint, to_mint, new_amount, slippage, provider)

        quote = {
            'inputMint': quote_response['inputMint'],
            'inAmount': float(quote_response['inAmount']) / 10**from_mint_decimals,
            'outputMint': quote_response['outputMint'],
            'outAmount': float(quote_response['outAmount']) / 10**to_mint_decimals,
            'minimumReceived': float(quote_response['minimumReceived']) / 10**to_mint_decimals,
            'slippage': quote_response['slippage'] / 100,
            'priceImpactPercent': float(quote_response['priceImpactPercent']),
        }

        return quote

    async def bulk_quote(self, from_mint: str, to_mint: str, amount: float, slippage: float, providers: List[str], from_mint_decimals: int = 9, to_mint_decimals: int = 9) -> List[BulkQuoteResponseMap]:
        tasks = []
        for provider in providers:
            task = self.get_quote(from_mint, to_mint, amount, slippage, provider, from_mint_decimals, to_mint_decimals)
            tasks.append(task)
        
        quotes = await asyncio.gather(*tasks)
        
        bulk_quotes = [{'provider': provider, 'quote': quote} for provider, quote in zip(providers, quotes)]
        
        return bulk_quotes