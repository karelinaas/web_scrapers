import time
from typing import Any

from constants import INFO_QUERIES_EXEC_TIME
from scrapers.base import BaseScraper


def _print_execution_time(method: str, count: int, start_time: float):
    print(
        INFO_QUERIES_EXEC_TIME.format(
            method=method,
            requests_count=count,
            seconds=(time.time() - start_time),
        )
    )


def batch_runner_helper(
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


async def abatch_runner_helper(
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
