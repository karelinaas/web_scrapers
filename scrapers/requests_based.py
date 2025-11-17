from typing import Any

import requests

from scrapers.base import BaseScraper


class RequestsBasedScraper(BaseScraper):
    def single_get_request(self, url: str) -> Any:
        response = requests.get(url)
        print(url, response.status_code)

    def single_post_request(self, url: str, data: dict[str, Any]):
        response = requests.post(url, json=data)
        print(url, response.status_code)

    def batch_get_requests(self, urls: list[str]):
        for url in urls:
            self.single_get_request(url)

    def batch_post_requests(self, request_data: list[tuple[str, dict[str, Any]]]):
        for url, data in request_data:
            self.single_post_request(url, data)
