import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"

    def start_requests(self):
        urls = ["https://www.sacred-texts.com/the/iu/iu000.htm"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # TODO: Steps for parsing
        #   1. Only scrape the html body since html is valid markdown
        #   2. Set rule to only crawl through sacred-texts domain
        #   3. Research sequence of crawling so that the books are
        #      added in order (maybe just crawl & gather ALL of the links on
        #      the domain & sort them before parsing each url)
        #   4. Init .md file stream with io
        #   5. Start at index.htm page of the book & continue iterating
        #      through each of the pages (e.g. /the/iu/iu#.htm) where #
        #      increases. Add each page/chapter of book to file stream
        #      - 5.1 Capture book title from index.htm and save as var for
        #        later use as the book's file name
        #   6. Continue iteration until 404 Status Code (this is end of book)
        #   7. Finally save .md file stream to Obsidian Vault
        #   8. Continue crawling to next book

        item = {}
        item["url"] = response.url
        # extract basic body
        item["body"] = "\n".join(response.xpath("//text()").extract())
        # or better just save whole source
        item["source"] = response.body
        yield item
