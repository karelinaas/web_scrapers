import asyncio

from demo_utils import demo_async_scraper, demo_sync_scraper
from scrapers import AiohttpBasedScraper, HttpxBasedScraper, MultiThreadRequestsBasedScraper


async def main():
    await demo_async_scraper(AiohttpBasedScraper)
    await demo_async_scraper(HttpxBasedScraper)
    demo_sync_scraper()
    demo_sync_scraper(MultiThreadRequestsBasedScraper, many_queries=True)

if __name__ == "__main__":
    asyncio.run(main())
