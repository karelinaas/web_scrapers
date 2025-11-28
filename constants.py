BASE_URL = "https://httpbingo.org/"

GET_REQUESTS_URLS = [
    "get",
    "status/200",
    "status/201",
    "status/202",
    "status/400",
    "status/404",
    "status/500",
    "headers",
    "ip",
    "user-agent",
    "cache",
    "response-headers",
    "html",
    "json",
    "xml",
    "cookies",
]

POST_REQUESTS_DATA = [
    ("post", {"example": "value", "var": 1}),
    ("status/200", {"example": "value", "var": 1}),
    ("status/201", {"example": "value", "var": 1}),
    ("status/202", {"example": "value", "var": 1}),
    ("status/400", {"val": 0.123}),
    ("status/404", {"val": 0.123}),
    ("status/500", {"val": 0.123}),
    ("response-headers", {"freeform": "dummy"}),
    ("redirect_to", {"url": "https://www.google.com/", "status_code": 200}),
    ("redirect_to", {"url": "https://qwertyuioppahasdgksfk.com/", "status_code": 404}),
]

INFO_QUERIES_EXEC_TIME = "{method} {requests_count} queries in {seconds} seconds\n"
INFO_SCRAPER_TEST_START = ("-" * 15) + " {scraper_class} " + ("-" * 15)
INFO_SCRAPER_TEST_END = "-" * 80

MAX_WORKERS = 30
