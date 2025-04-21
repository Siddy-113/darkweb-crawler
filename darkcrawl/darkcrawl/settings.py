# settings.py

BOT_NAME = "darkcrawl"

SPIDER_MODULES = ["darkcrawl.spiders"]
NEWSPIDER_MODULE = "darkcrawl.spiders"

# Obey robots.txt rules (usually disabled for dark web)
ROBOTSTXT_OBEY = False

# Limit concurrent requests and add delay to avoid flooding
CONCURRENT_REQUESTS = 3
DOWNLOAD_DELAY = 2  # seconds

# Concurrent requests per domain/IP
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# User-Agent to mimic a real browser
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"

# Disable cookies unless needed
COOKIES_ENABLED = False

# Enable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'darkcrawl.middlewares.TorProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 400,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,
}


# Example Tor proxy (enable only if using Tor)
# HTTP_PROXY = 'http://127.0.0.1:8118'  # if using privoxy
# HTTPS_PROXY = 'http://127.0.0.1:8118'

# Feed export to JSON
FEEDS = {
    "output.json": {
        "format": "json",
        "encoding": "utf8",
        "store_empty": False,
        "indent": 4,
    }
}

# Encoding
FEED_EXPORT_ENCODING = "utf-8"

# Twisted reactor (compatible with asyncio)
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

# Optional: Disable Telnet console if not needed
TELNETCONSOLE_ENABLED = False

# Log level
LOG_LEVEL = 'INFO'


