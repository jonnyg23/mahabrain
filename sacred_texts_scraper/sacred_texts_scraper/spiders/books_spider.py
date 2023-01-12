import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"

    def start_requests(self):
        urls = ["https://www.sacred-texts.com/the/iu/iu000.htm"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # TODO: Update with correct values in HTML scrape
        yield {
            "title": response.xpath("//h1").get(),
            "subtitle": response.xpath("//h2").get(),
            "header": response.xpath("//h3").get(),
            "body": response.xpath("//p").getall(),
        }
