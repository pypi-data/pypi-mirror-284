from .quote import Quote
from .swap import Swap

class Spiderswap:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = 'https://api.spiderswap.io/spider-api/v1'
        self.quote = Quote(self.base_url, self.api_key)
        self.swap = Swap(self.base_url, self.api_key)

__all__ = ["Spiderswap", "Quote", "Swap"]