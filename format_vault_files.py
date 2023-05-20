import os
import re
from typing import Callable
import unicodedata
from markdownify import markdownify

UNICODE_CHARS_FOUND = set()
NAMES = []


def html2md(file_path: str, text: str):
    """Loops through folder structure and converts all .md files that contain
    html into pure markdown files
    """

    html = markdownify(text)
    return html


def replace_newlines(file_path: str, text: str) -> str:
    """Replaces many new lines breaks with a single line break for
    readability"""

    def xnl(count):
        return "\n" * count

    new_line_blacklist = [xnl(count) for count in range(3, 15)]
    for blacklisted_nl in new_line_blacklist:
        if blacklisted_nl in text:
            text = re.sub(blacklisted_nl, "\n", text)
    return text


def find_control_unicode_chars(file_path: str, text: str):
    """Finds all unicode characters in the 'control' category"""
    blacklist = {  # Don't show these
        "\n",
    }
    # control_chars = set()

    for idx, char in enumerate(text):
        if unicodedata.category(char) == "Cc" and char not in blacklist:
            formatted_char = f"U+{ord(char):04X}"
            if formatted_char not in UNICODE_CHARS_FOUND:
                NAMES.append(
                    f"{formatted_char} ({file_path}) \n---after-- {text[idx+1:idx+11]}"
                )
            UNICODE_CHARS_FOUND.add(formatted_char)
    # if control_chars:
    #     print(f"{file_path} contains: {control_chars}")


def replace_unicode(file_path: str, text: str) -> str:
    """Replaces all unicode terms found in files with replacement"""
    mapping = {
        "\u0091": "\u0060",  # ` Grave Accent
        "\u009C": "\u0153",  # oe in Latin
        "\u009F": "\u0178",  # Ÿ
        "\u0086": "\u2020",  # † (dagger)
        "\u0087": "\u2021",  # ‡ (double dagger)
        "\u0096": "\u2013",  # – (en)
        "\u008C": "\u0152",  # Œ OE capital in Latin
        "\u0095": "\u2022",  # • bullet
        "\u0093": "\u0022",  # Left Double Quotation Mark
        "\u0094": "\u0022",  # Right Double Quotation Mark
        "\u0085": "\u2026",  # ... Horizontal Ellipsis
        "\u0009": "\u25E6",  # White Bullet Point
        "\u009A": "\u0161",  # Latin small letter S with Caron
        "\u0083": "\u0192",  # Latin small letter F with Hook
        "\u0089": "\u2023",  # Per Mille Sign {permille, per thousand}
        "\u008A": "\u0160",  # Latin capital letter S with Caron
        "\u0088": "\u02C6",  # Modifier Letter Circumflex Accent
    }

    def find_occurrences(text: str, unicode_term: str):
        occurrences = []
        index = 0
        while True:
            index = text.find(unicode_term, index)
            if index == -1:
                break
            occurrences.append(index)
            index += 1
        return occurrences

    for unicode_term, replacement in mapping.items():
        occurrences = len(find_occurrences(text, unicode_term))
        if occurrences != 0:
            # print(file_path, f"->{occurrences} occurrences")
            text = text.replace(unicode_term, replacement)
            # occurrences_left = len(find_occurrences(text, unicode_term))
    return text


def apply_func_to_files(vault_location: str, func: Callable, write=False):
    """Applies function to each file's text body"""
    for root, dirs, files in os.walk(vault_location):
        for filename in files:
            if filename[-3:] != ".md":
                continue

            file_path = os.path.join(root, filename)
            with open(file_path, "r+") as f:
                text = f.read()
                f.seek(0)
                try:
                    text = func(file_path, text)
                    if write:
                        f.write(text)
                        f.truncate()
                except Exception as e:
                    print(f"Exception: {e}", file_path)
                    continue


if __name__ == "__main__":
    vault_location = "../sacred_obsidian_vault/"

    # Run below to find all control unicode characters in vault
    func = find_control_unicode_chars
    write = False
    apply_func_to_files(vault_location=vault_location, func=func, write=write)
    print(f"Control Unicode chars found: {UNICODE_CHARS_FOUND}")
    print("NAMES:")
    [print(name) for name in NAMES]

    ## Run below to replace unicode characters
    # func = replace_unicode
    # write = True
    # apply_func_to_files(vault_location=vault_location, func=func, write=write)

