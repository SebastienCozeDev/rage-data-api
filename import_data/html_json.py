import json


def get_html_content(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html_content = f.read()
    return html_content


def save_data_to_json(data, filename="data.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
