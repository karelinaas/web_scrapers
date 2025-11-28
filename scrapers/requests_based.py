from concurrent.futures import ThreadPoolExecutor
from typing import Any

import requests

from constants import MAX_WORKERS
from scrapers.base import BaseScraper


class RequestsBasedScraper(BaseScraper):
    def single_get_request(self, url: str):
        response = requests.get(f"{self.base_url}{url}")
        print(url, response.status_code)

    def single_post_request(self, url: str, data: dict[str, Any]):
        response = requests.post(f"{self.base_url}{url}", json=data)
        print(url, response.status_code)

    def batch_get_requests(self, urls: list[str]):
        for url in urls:
            self.single_get_request(url)

    def batch_post_requests(self, request_data: list[tuple[str, dict[str, Any]]]):
        for url, data in request_data:
            self.single_post_request(url, data)


class MultiThreadRequestsBasedScraper(RequestsBasedScraper):
    def batch_get_requests(self, urls: list[str]):
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = [executor.submit(self.single_get_request, url) for url in urls]

            for future in futures:
                try:
                    result = future.result()
                except Exception:
                    print(result, "Error")

    def batch_post_requests(self, request_data: list[tuple[str, dict[str, Any]]]):
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = [executor.submit(self.single_post_request, *config) for config in request_data]

            for future in futures:
                try:
                    result = future.result()
                except Exception:
                    print(result, "Error")
