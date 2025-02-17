import scrapy
import json
from pathlib import Path

class BotsSpider(scrapy.Spider):
    name = "bots"
    allowed_domains = ["toscrape.com"]
    start_urls = [
        "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html",
        "https://books.toscrape.com/catalogue/category/books/romance_8/index.html",
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Extracting the category name from the URL (fiction, romance, etc.)
        category = response.url.split("/")[-2]
        
        # Extracting book details
        books = []
        for book in response.css("article.product_pod"):
            title = book.css("h3 a::attr(title)").get()
            price = book.css("p.price_color::text").get()
            availability = book.css("p.in_stock.availability::text").get().strip()
            url = book.css("h3 a::attr(href)").get()
            
            books.append({
                'title': title,
                'price': price,
                'availability': availability,
                'url': response.urljoin(url),  # Make the URL absolute
            })

        # Saving extracted data to a JSON file
        self.save_to_json(category, books)
        
        # Follow pagination links to crawl next pages if any
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)
    
    def save_to_json(self, category, books):
        # Define the filename as category.json (e.g., fiction.json)
        filename = f"books-{category}.json"
        
        # Check if file exists, if so, append to it
        if Path(filename).exists():
            with open(filename, "r") as file:
                existing_data = json.load(file)
            existing_data.extend(books)
            books = existing_data
        
        # Save the extracted books data to the file
        with open(filename, "w") as file:
            json.dump(books, file, indent=4)

        self.log(f"Saved {len(books)} books to {filename}")
