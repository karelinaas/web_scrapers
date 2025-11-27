import asyncio
import sys

from demo_utils import demo_async_scraper, demo_sync_scraper
from scrapers import AiohttpBasedScraper, HttpxBasedScraper, MultiThreadRequestsBasedScraper, RequestsBasedScraper


async def main(sys_argv: list[str]):
    scrapers_mapping = {
        "aiohttp": {
            "class": AiohttpBasedScraper,
            "is_async": True,
            "many_queries": None,
        },
        "httpx": {
            "class": HttpxBasedScraper,
            "is_async": True,
            "many_queries": None,
        },
        "requests": {
            "class": RequestsBasedScraper,
            "is_async": False,
            "many_queries": False,
        },
        "requests_multi": {
            "class": MultiThreadRequestsBasedScraper,
            "is_async": False,
            "many_queries": True,
        }
    }

    if "all" in sys_argv:
        sys_argv = scrapers_mapping.keys()

    for code in sys_argv:
        scraper_params = scrapers_mapping[code]
        if scraper_params["is_async"]:
            await demo_async_scraper(scraper_params["class"])
        else:
            demo_sync_scraper(scraper_params["class"], many_queries=scraper_params["many_queries"])


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:] or ["all"]))
