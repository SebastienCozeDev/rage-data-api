"""
This file contains the util functions to extract data from the source files and save it into the JSON files.
"""

import json


def get_html_content(filepath):
    """
    Get the HTML content.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        html_content = f.read()
    return html_content


def save_data_to_json(data, filename="data.json"):
    """
    Save data into JSON file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
