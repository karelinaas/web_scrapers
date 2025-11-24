import asyncio
import sys

from demo_utils import demo_async_scraper, demo_sync_scraper
from scrapers import AiohttpBasedScraper, HttpxBasedScraper, MultiThreadRequestsBasedScraper

async def main(sys_argv: list[str]):
    if any(code in sys_argv for code in ["aiohttp", "all"]):
        await demo_async_scraper(AiohttpBasedScraper)
    if any(code in sys_argv for code in ["httpx", "all"]):
        await demo_async_scraper(HttpxBasedScraper)
    if any(code in sys_argv for code in ["requests", "all"]):
        demo_sync_scraper()
    if any(code in sys_argv for code in ["requests_multi", "all"]):
        demo_sync_scraper(MultiThreadRequestsBasedScraper, many_queries=True)

if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:] or ["all"]))
