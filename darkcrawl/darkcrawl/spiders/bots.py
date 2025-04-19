import scrapy
import re
from darkcrawl.items import DarkcrawlItem

class BotsSpider(scrapy.Spider):
    name = "bots"
    allowed_domains = ["something.onion"]
    start_urls = ["http://something.onion"]

    custom_settings = {
        "FEEDS": {
            "output.json": {"format": "json", "encoding": "utf8"},  # Save output in JSON
        },
        "DOWNLOAD_DELAY": 2,
        "CONCURRENT_REQUESTS": 3,
        "ROBOTSTXT_OBEY": False,
        "DOWNLOADER_MIDDLEWARES":{
            'scrapy.downloadmiddlewares.httpproxy.HttpProxyMiddleware':1,
            'darkcrawl.middlewares.TorProxyMiddleware':100, #using tor for scraping
        },
    }

    def parse(self, response):
        item = DarkcrawlItem()
        item['title'] = response.xpath('//title/text()').get()
        item['url'] = response.url

        text = response.text
        ip_match = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)
        email.match = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
        
        item['ip'] = ip_match
        item['email'] = email_match

        yield item

        #follow all internal links
        for href in response.css('a::attr(href)').getall():
            if href.startswith('/'):
                href=response.urljoin(href)
            if self.allowed_domains[0] in href:
                yield response.follow(href, self.parse)

