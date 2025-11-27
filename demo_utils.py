import time
from typing import Any

from constants import (
    BASE_URL,
    GET_REQUESTS_URLS,
    INFO_QUERIES_EXEC_TIME,
    INFO_SCRAPER_TEST_END,
    INFO_SCRAPER_TEST_START,
    POST_REQUESTS_DATA,
)
from scrapers.base import BaseScraper


def _print_execution_time(method: str, count: int, start_time: float):
    print(
        INFO_QUERIES_EXEC_TIME.format(
            method=method,
            requests_count=count,
            seconds=(time.time() - start_time),
        )
    )


def _batch_runner_helper(
    scraper: BaseScraper,
    requests_data: list[tuple[str, dict[str, Any]]] | list[str],
    method: str = "GET",
):
    start_time = time.time()

    if method == "GET":
        scraper.batch_get_requests(requests_data)
    elif method == "POST":
        scraper.batch_post_requests(requests_data)
    else:
        raise TypeError(f"Invalid method: {method}")

    _print_execution_time(method, len(requests_data), start_time)


async def _abatch_runner_helper(
    async_scraper: BaseScraper,
    requests_data: list[tuple[str, dict[str, Any]]] | list[str],
    method: str = "GET",
):
    start_time = time.time()

    async with async_scraper as scraper:
        if method == "GET":
            await scraper.batch_get_requests(requests_data)
        elif method == "POST":
            await scraper.batch_post_requests(requests_data)
        else:
            raise TypeError(f"Invalid method: {method}")

    _print_execution_time(method, len(requests_data), start_time)


def demo_sync_scraper(scraper_class: type[BaseScraper], *, many_queries: bool = False):
    print(INFO_SCRAPER_TEST_START.format(scraper_class=scraper_class))
    scraper = scraper_class(BASE_URL)

    get_requests = GET_REQUESTS_URLS * 6 if many_queries else GET_REQUESTS_URLS
    post_requests = POST_REQUESTS_DATA * 10 if many_queries else POST_REQUESTS_DATA

    _batch_runner_helper(scraper, get_requests)
    _batch_runner_helper(scraper, post_requests, "POST")

    print(INFO_SCRAPER_TEST_END)


async def demo_async_scraper(scraper_class: type[BaseScraper]):
    print(INFO_SCRAPER_TEST_START.format(scraper_class=scraper_class))
    async_scraper = scraper_class(BASE_URL)

    get_requests = GET_REQUESTS_URLS * 6
    post_requests = POST_REQUESTS_DATA * 10

    await _abatch_runner_helper(async_scraper, get_requests)
    await _abatch_runner_helper(async_scraper, post_requests, "POST")

    print(INFO_SCRAPER_TEST_END)
