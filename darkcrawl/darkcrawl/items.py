import scrapy


class DarkcrawlItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    ip = scrapy.Field()
    email = scrapy.Field()

