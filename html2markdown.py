import os
import re
from markdownify import markdownify


def html2md():
    """Loops through folder structure and converts all .md files that contain
    html into pure markdown files
    """

    for root, dirs, files in os.walk("./sacred_obsidian_vault/"):
        for filename in files:
            if filename[-3:] != ".md":
                continue

            file_path = os.path.join(root, filename)

            with open(file_path, "r+") as f:
                text = f.read()
                f.seek(0)
                try:
                    html = markdownify(text)
                    f.write(html)
                    f.truncate()
                except Exception:
                    print("Exception: ", file_path)
                    continue


def replace_newlines():
    """Replaces many new lines breaks with a single line break for
    readability"""
    for root, dirs, files in os.walk("./sacred_obsidian_vault/"):
        for filename in files:
            if filename[-3:] != ".md":
                continue

            file_path = os.path.join(root, filename)
            with open(file_path, "r+") as f:
                text = f.read()
                f.seek(0)
                xnl = lambda count: "\n" * count
                new_line_blacklist = [xnl(count) for count in range(3, 15)]
                try:
                    for blacklisted_nl in new_line_blacklist:
                        if blacklisted_nl in text:
                            text = re.sub(blacklisted_nl, "\n", text)
                    f.write(text)
                    f.truncate()
                except Exception:
                    print("Exception: ", file_path)
                    continue


if __name__ == "__main__":
    # Run Step 1 first & then comment out step 1 to run step 2
    # You may have to change line 11 & 33 above to path of vault
    # Step 1: Convert html to md
    html2md()

    # Step 2: Replace any consecutive 4+ new lines to a single new line \n
    # for better readability.
    # replace_newlines()
