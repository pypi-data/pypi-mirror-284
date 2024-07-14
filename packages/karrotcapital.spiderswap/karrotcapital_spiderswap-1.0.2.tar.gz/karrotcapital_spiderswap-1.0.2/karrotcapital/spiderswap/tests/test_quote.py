import pytest
import asyncio
from karrotcapital.spiderswap import Spiderswap

@pytest.fixture
def spiderswap():
    api_key = '8fd8b157e86f072b5cfaa7df4740985b'
    return Spiderswap(api_key)

@pytest.mark.asyncio
async def test_get_quote_raw(spiderswap):
    from_mint = 'So11111111111111111111111111111111111111112'
    to_mint = 'AT79ReYU9XtHUTF5vM6Q4oa9K8w7918Fp5SU7G1MDMQY'
    amount = 1000000  # in lamports
    slippage = 50  # in bps
    provider = 'raydium'
    
    # Mock the aiohttp session and response
    async def mock_get(url, params, headers):
        class MockResponse:
            status = 200
            async def json(self):
                return {
                    'data': {
                        'inputMint': from_mint,
                        'inAmount': amount,
                        'outputMint': to_mint,
                        'outAmount': 950000,  # example value
                        'minimumReceived': 900000,  # example value
                        'slippage': slippage,
                        'priceImpactPercent': '0.5'  # example value
                    }
                }
        return MockResponse()

    spiderswap.quote.get_quote_raw.__globals__['aiohttp'].ClientSession().get = mock_get
    
    result = await spiderswap.quote.get_quote_raw(from_mint, to_mint, amount, slippage, provider)
    
    assert result['inputMint'] == from_mint
    assert int(result['inAmount']) == amount
    assert result['outputMint'] == to_mint
    assert int(result['slippage']) == slippage

@pytest.mark.asyncio
async def test_get_quote(spiderswap):
    from_mint = 'So11111111111111111111111111111111111111112'
    to_mint = 'AT79ReYU9XtHUTF5vM6Q4oa9K8w7918Fp5SU7G1MDMQY'
    amount = 1.0  # in tokens
    slippage = 0.5  # in percentage
    provider = 'raydium'
    from_mint_decimals = 9
    to_mint_decimals = 9

    # Mock the get_quote_raw method
    async def mock_get_quote_raw(from_mint, to_mint, new_amount, slippage, provider):
        return {
            'inputMint': from_mint,
            'inAmount': new_amount,
            'outputMint': to_mint,
            'outAmount': 950000000,  # example value in lamports
            'minimumReceived': 900000000,  # example value in lamports
            'slippage': slippage,
            'priceImpactPercent': '0.5'  # example value
        }

    spiderswap.quote.get_quote_raw = mock_get_quote_raw

    result = await spiderswap.quote.get_quote(from_mint, to_mint, amount, slippage, provider, from_mint_decimals, to_mint_decimals)
    
    assert result['inputMint'] == from_mint
    assert result['inAmount'] == amount
    assert result['outputMint'] == to_mint
    assert result['outAmount'] == 0.95  # converted from lamports
    assert result['minimumReceived'] == 0.9  # converted from lamports
    assert result['slippage'] == 0.5  # converted from bps
    assert result['priceImpactPercent'] == 0.5

@pytest.mark.asyncio
async def test_bulk_quote(spiderswap):
    from_mint = 'So11111111111111111111111111111111111111112'
    to_mint = 'AT79ReYU9XtHUTF5vM6Q4oa9K8w7918Fp5SU7G1MDMQY'
    amount = 1.0  # in tokens
    slippage = 0.5  # in percentage
    providers = ['raydium', 'meteora']
    from_mint_decimals = 9
    to_mint_decimals = 9

    # Mock the get_quote method
    async def mock_get_quote(from_mint, to_mint, amount, slippage, provider, from_mint_decimals, to_mint_decimals):
        return {
            'inputMint': from_mint,
            'inAmount': amount,
            'outputMint': to_mint,
            'outAmount': 0.95,  # example value in tokens
            'minimumReceived': 0.9,  # example value in tokens
            'slippage': slippage,
            'priceImpactPercent': 0.5  # example value
        }

    spiderswap.quote.get_quote = mock_get_quote

    result = await spiderswap.quote.bulk_quote(from_mint, to_mint, amount, slippage, providers, from_mint_decimals, to_mint_decimals)

    assert len(result) == 2
    assert result[0]['provider'] == 'raydium'
    assert result[1]['provider'] == 'meteora'
    assert result[0]['quote']['inputMint'] == from_mint
    assert result[0]['quote']['inAmount'] == amount
    assert result[0]['quote']['outputMint'] == to_mint
    assert result[0]['quote']['outAmount'] == 0.95
    assert result[0]['quote']['minimumReceived'] == 0.9
    assert result[0]['quote']['slippage'] == 0.5
    assert result[0]['quote']['priceImpactPercent'] == 0.5
