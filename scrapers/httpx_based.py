import asyncio
from types import TracebackType
from typing import Any

import httpx

from scrapers.base import BaseScraper


class HttpxBasedScraper(BaseScraper):
    client: httpx.AsyncClient | None

    def __init__(self, base_url: str):
        super().__init__(base_url)
        self.client = None

    async def __aenter__(self):
        self.client = httpx.AsyncClient()
        return self

    async def __aexit__(self, exc_type: BaseException, exc_val: BaseException, exc_tb: TracebackType):
        if self.client:
            await self.client.aclose()

    async def single_get_request(self, url: str):
        response = await self.client.get(f"{self.base_url}{url}")
        print(url, response.status_code)

    async def single_post_request(self, url: str, data: dict[str, Any]):
        response = await self.client.post(f"{self.base_url}{url}", json=data)
        print(url, response.status_code)

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
