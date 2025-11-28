import asyncio

from constants import INFO_SCRAPER_TEST_END, INFO_SCRAPER_TEST_START


def scraper_demo_decorator(func):
    def wrapper(*args, **kwargs):
        scraper_class = args[0]

        print(INFO_SCRAPER_TEST_START.format(scraper_class=scraper_class))

        try:
            result = func(*args, **kwargs)
            return result
        finally:
            print(INFO_SCRAPER_TEST_END)

    async def async_wrapper(*args, **kwargs):
        scraper_class = args[0]

        print(INFO_SCRAPER_TEST_START.format(scraper_class=scraper_class))

        try:
            result = await func(*args, **kwargs)
            return result
        finally:
            print(INFO_SCRAPER_TEST_END)

    if asyncio.iscoroutinefunction(func):
        return async_wrapper
    return wrapper
