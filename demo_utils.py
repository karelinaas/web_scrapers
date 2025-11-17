import time

from constants import BASE_URL, GET_REQUESTS_URLS, POST_REQUESTS_DATA
from scrapers.base import BaseScraper
from scrapers import RequestsBasedScraper

async def demo_async_scraper(scraper_class: type[BaseScraper]):
    print("-" * 10, scraper_class, "Scraper", "-" * 10)
    async_scraper = scraper_class(BASE_URL)

    get_requests = GET_REQUESTS_URLS * 6
    post_requests = POST_REQUESTS_DATA * 10

    start_time_get = time.time()

    async with async_scraper as scraper:
        await scraper.batch_get_requests(get_requests)

    print(f"GET {len(get_requests)} queries in {(time.time() - start_time_get)} seconds")

    start_time_post = time.time()

    async with async_scraper as scraper:
        await scraper.batch_post_requests(post_requests)

    print(f"POST {len(post_requests)} queries in {(time.time() - start_time_post)} seconds")
    print("-" * 80)


def demo_sync_scraper():
    print("-" * 10, "Requests Scraper", "-" * 10)
    scraper = RequestsBasedScraper(BASE_URL)

    get_requests = GET_REQUESTS_URLS
    post_requests = POST_REQUESTS_DATA

    start_time_get = time.time()

    scraper.batch_get_requests(get_requests)

    print(f"GET {len(get_requests)} queries in {(time.time() - start_time_get)} seconds")

    start_time_post = time.time()

    scraper.batch_post_requests(post_requests)

    print(f"POST {len(post_requests)} queries in {(time.time() - start_time_post)} seconds")
    print("-" * 80)
