from abc import abstractmethod, ABC
from typing import Any


class BaseScraper(ABC):
    base_url: str

    def __init__(self, base_url: str):
        self.base_url = base_url

    @abstractmethod
    def single_get_request(self, url: str):
        raise NotImplementedError

    @abstractmethod
    def single_post_request(self, url: str, data: dict[str, Any]):
        raise NotImplementedError

    @abstractmethod
    def batch_get_requests(self, urls: list[str]):
        raise NotImplementedError

    @abstractmethod
    def batch_post_requests(self, request_data: list[tuple[str, dict[str, Any]]]):
        raise NotImplementedError
