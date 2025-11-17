import asyncio
from types import TracebackType
from typing import Any

import aiohttp

from scrapers.base import BaseScraper


class AiohttpBasedScraper(BaseScraper):
    session: aiohttp.ClientSession | None

    def __init__(self, base_url: str):
        super().__init__(base_url)
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type: BaseException, exc_val: BaseException, exc_tb: TracebackType):
        if self.session:
            await self.session.close()

    async def single_get_request(self, url: str):
        async with self.session.get(url) as response:
            print(url, response.status)

    async def single_post_request(self, url: str, data: dict[str, Any]):
        async with self.session.post(url, json=data) as response:
            print(url, response.status)

    async def batch_get_requests(self, urls: list[str]):
        tasks = []
        for url in urls:
            tasks.append(self.single_get_request(url))
        return await asyncio.gather(*tasks, return_exceptions=True)

    async def batch_post_requests(self, request_data: list[tuple[str, dict[str, Any]]]):
        tasks = []
        for url, data in request_data:
            tasks.append(self.single_post_request(url, data))
        return await asyncio.gather(*tasks, return_exceptions=True)
