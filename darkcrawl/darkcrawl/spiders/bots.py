import scrapy
import re
from darkcrawl.items import DarkcrawlItem

class BotsSpider(scrapy.Spider):
    name = "bots"
    allowed_domains = ["duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion"]
    start_urls = ["http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/"]


    def parse(self, response):
        item = DarkcrawlItem()
        item['title'] = response.xpath('//title/text()').get()
        item['url'] = response.url

        text = response.text
        ip_match = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)
        email_match = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)

        item['ip'] = ip_match
        item['email'] = email_match

        yield item

        # follow all internal links
        for href in response.css('a::attr(href)').getall():
            if href.startswith('/'):
                href = response.urljoin(href)
            if self.allowed_domains[0] in href:
                yield response.follow(href, self.parse)

