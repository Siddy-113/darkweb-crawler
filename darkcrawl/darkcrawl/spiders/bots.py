import scrapy

class BotsSpider(scrapy.Spider):
    name = "bots"
    allowed_domains = ["books.toscrape.com"]  # Change to actual target domain
    start_urls = [
        "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html",
        "https://books.toscrape.com/catalogue/category/books/romance_8/index.html",
    ]

    custom_settings = {
        "DOWNLOAD_DELAY": 2,  # Prevents getting blocked
        "CONCURRENT_REQUESTS": 3,  # Adjust based on site responsiveness
        "ROBOTSTXT_OBEY": False
    }

    def parse(self, response):
        for post in response.css("div.post"):  # Adjust selector based on site
            yield {
                "title": post.css("h2.title::text").get(),
                "author": post.css("span.author::text").get(),
                "date": post.css("span.date::text").get(),
                "content": post.css("div.content::text").get(),
                "link": response.urljoin(post.css("a::attr(href)").get()),
            }

        # Follow pagination links
        next_page = response.css("a.next::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
