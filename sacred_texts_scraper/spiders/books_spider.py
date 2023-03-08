from pathlib import Path
import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["sacred-texts.com"]

    def start_requests(self):
        urls = ["https://www.sacred-texts.com/the/iu/iu000.htm"]
        # urls = ["https://www.sacred-texts.com/the"]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        base_path = "../../sacred_obsidian_vault"
        endpoint = response.url.replace("https://www.sacred-texts.com/", "")

        # Add non-book containing folders
        if "." not in endpoint:
            # Create folders if they don't exist
            folder_path = f"{base_path}/{endpoint}"

            if folder_path[-1] == "/":
                Path(folder_path[:-1]).mkdir(parents=True, exist_ok=True)
            else:
                Path(folder_path).mkdir(parents=True, exist_ok=True)

            yield None

        # Add book
        else:
            # Create parent folders if they don't exist
            filepath = f"{base_path}/{endpoint.split('.')[0]}.md"
            folder_path = "/".join(filepath.split("/")[:-1])
            Path(folder_path).mkdir(parents=True, exist_ok=True)
            print('\n\n', filepath, folder_path, '\n\n')

            # Create .md file at path
            with Path(filepath).open(mode="wb") as f:
                f.write(response.body)

            yield None
