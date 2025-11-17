from .aiohttp_based import AiohttpBasedScraper
from .httpx_based import HttpxBasedScraper
from .requests_based import RequestsBasedScraper

__all__ = [
    "AiohttpBasedScraper",
    "HttpxBasedScraper",
    "RequestsBasedScraper",
]
