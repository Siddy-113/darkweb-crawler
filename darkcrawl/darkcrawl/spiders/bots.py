import scrapy

class BotsSpider(scrapy.Spider):
    name = "bots"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/category/books/fiction_10/index.html"]

    custom_settings = {
        "FEEDS": {
            "output.json": {"format": "json", "encoding": "utf8"},  # Save output in JSON
        },
        "DOWNLOAD_DELAY": 2,
        "CONCURRENT_REQUESTS": 3,
        "ROBOTSTXT_OBEY": False
    }

    def parse(self, response):
        for book in response.css("article.product_pod"):
            yield {
                "title": book.css("h3 a::attr(title)").get(),
                "price": book.css("p.price_color::text").get(),
                "availability": book.css("p.instock.availability::text").get().strip(),
                "link": response.urljoin(book.css("h3 a::attr(href)").get()),
            }

        # Follow pagination links
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
