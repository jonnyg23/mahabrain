from pathlib import Path
import scrapy
from scrapy.linkextractors import LinkExtractor


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["sacred-texts.com"]
    # start_urls = ["https://www.sacred-texts.com/the/iu/iu000.htm"]
    start_urls = ["https://www.sacred-texts.com"]

    def parse(self, response):
        base_path = "./sacred_obsidian_vault"
        endpoint = response.url.replace("https://www.sacred-texts.com/", "")

        # Add non-book containing folders
        if "." not in endpoint:
            # Create folders if they don't exist
            folder_path = f"{base_path}/{endpoint}"
            Path(folder_path[:-1]).mkdir(parents=True, exist_ok=True)

            links = self._next_links(response, base_path)

            yield from response.follow_all(links, callback=self.parse)

        # Add book
        else:
            # Create parent folders if they don't exist
            filepath = f"{base_path}/{endpoint.split('.')[0]}.md"
            folder_path = "/".join(filepath.split("/")[:-1])
            Path(folder_path).mkdir(parents=True, exist_ok=True)

            # Create .md file at path
            with Path(filepath).open(mode="w") as f:
                f.write(response.css("BODY").get())

            links = self._next_links(response, base_path)

            yield from response.follow_all(links, callback=self.parse)

    def _next_links(self, response, base_path) -> list:
        link_extractor = LinkExtractor(
            allow_domains="sacred-texts.com",
            deny_extensions=[
                "pdf",
                "jpg",
                "jpeg",
                "svg",
                "png",
                "mov",
                "mp4",
                "mp3",
                "avi",
                "zip",
                "csv",
                "#",
            ],
        )
        links = []
        for link in link_extractor.extract_links(response):
            # Filter link list to reduce calls
            if "#" not in link.url.split(".")[-1]:
                local_path_no_ext = (
                    f"{base_path}{link.url.replace('https://www.sacred-texts.com', '')}"
                )
                local_link = local_path_no_ext.replace(".htm", ".md")

                if not Path(local_link).exists():
                    links.append(link.url)

        return links
