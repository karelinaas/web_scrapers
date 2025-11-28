from constants import BASE_URL, GET_REQUESTS_URLS, POST_REQUESTS_DATA
from demo_utils.decorators import scraper_demo_decorator
from demo_utils.helpers import abatch_runner_helper, batch_runner_helper
from scrapers.base import BaseScraper


@scraper_demo_decorator
def demo_sync_scraper(scraper_class: type[BaseScraper], *, many_queries: bool = False):
    scraper = scraper_class(BASE_URL)

    get_requests = GET_REQUESTS_URLS * 6 if many_queries else GET_REQUESTS_URLS
    post_requests = POST_REQUESTS_DATA * 10 if many_queries else POST_REQUESTS_DATA

    batch_runner_helper(scraper, get_requests)
    batch_runner_helper(scraper, post_requests, "POST")


@scraper_demo_decorator
async def demo_async_scraper(scraper_class: type[BaseScraper]):
    async_scraper = scraper_class(BASE_URL)

    get_requests = GET_REQUESTS_URLS * 6
    post_requests = POST_REQUESTS_DATA * 10

    await abatch_runner_helper(async_scraper, get_requests)
    await abatch_runner_helper(async_scraper, post_requests, "POST")
