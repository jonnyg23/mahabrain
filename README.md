<img src="ISTA_OV.png" alt="ISTA_OV.png" width="450px" />

# mahabrain :brain: :books:

## Overview

A web scrape of [sacred-texts.com](www.sacred-texts.com) into an Obsidian Vault

### Obsidian Vault Info

- Size: **~2.22 GB**
- File Types: **.md**
- The vault in this repo
  ([sacred_obsidian_vault](https://github.com/jonnyg23/mahabrain/tree/main/sacred_obsidian_vault))
  was scraped in March 2023 when the latest ISTA flash drive edition was 9.0.

## Steps to Open in Obsidian

1. Download
   [sacred_obsidian_vault](https://github.com/jonnyg23/mahabrain/tree/main/sacred_obsidian_vault)
   from this repo
   - **Do not run Scrapy the web-scraper script** as this may be considered
     [abuse](https://sacred-texts.com/abuse.htm) and increase cost to run the
     sacred-texts website. Only download from the pre-scraped vault above.
2. Download latest Obsidian.md version [here](https://obsidian.md/)
3. Open Obsidian & choose `Open folder as vault` option
4. Select the recently downloaded sacred_obsidian_vault
5. Allow Obsidian to finish indexing the 120k+ files
6. 🎉 You're good to go! Enjoy exploring!


## Steps Used to Run Scraper (Only Use If Necessary)

### Requirements

- Python 3.7+
- Works on Linux, Windows, macOS, BSD


### Install

Run code below in project root directory in pyenv or venv

```bash
pip install -r requirements.txt
```

### Run Scrapy

Execute the following to begin scraping
[sacred-texts.com](www.sacred-texts.com) into **sacred_obsidian_vault**
top-level directory:

```bash
scrapy crawl books
```

> :information_source: Note: This web scrape may take **up to 1 hour to complete**.