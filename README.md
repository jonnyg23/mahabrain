<img src="ISTA_OV.png" alt="ISTA_OV.png" width="450px" />

# mahabrain :brain: :books:

## Overview

A web scrape of [sacred-texts.com](www.sacred-texts.com) into an Obsidian Vault

### Obsidian Vault Info

- Size: **~2.22 GB**
- File Types: **.md**

## Requirements

- Python 3.7+
- Works on Linux, Windows, macOS, BSD


## Install

Run code below in project root directory in pyenv or venv

```bash
pip install -r requirements.txt
```

## Run Scrapy

Execute the following to begin scraping
[sacred-texts.com](www.sacred-texts.com) into **sacred_obsidian_vault**
top-level directory:

```bash
scrapy crawl books
```

> :information_source: Note: This web scrape may take **up to 1 hour to complete**.

## Hosted on GitHub Pages following [Quartz](https://quartz.jzhao.xyz/)

- The **sacred_obsidian_vault** folder is opened in Obsidian & is indexed.
  After indexing, these steps were taken in order for the vault
  to work with Quartz:
  - Open Obsidian Settings > Files & Links and look for these two items:
    - Set the New link format to Absolute Path in vault. If you have a completely flat vault (no folders), this step isn’t necessary.
    - Turn on the Automatically update internal links setting.


- The root Quartz repo is then given access to the **sacred_obsidian_vault** by
placing this vault/folder inside **/content**.