import json
import re
from bs4 import BeautifulSoup
from import_data.html_json import get_html_content, save_data_to_json

class Importer:
    def __init__(self, model_name):
        self.model_name = model_name

    @staticmethod
    def extract_id(item, blip_data):
        gallerytext = item.find("div", class_="gallerytext")
        if gallerytext:
            id_match = re.search(r"ID:\s*(\d+)", gallerytext.get_text())
            if id_match:
                blip_data["id"] = int(id_match.group(1))

    @staticmethod
    def extract_name_and_hash(item, blip_data):
        gallerytext = item.find("div", class_="gallerytext")
        if gallerytext:
            text = gallerytext.get_text(separator="\n")
            name_match = re.search(r"Name:\s*([^\n]+)", text)
            hash_match = re.search(r"Hash:\s*(0x[0-9A-Fa-f]+)", text)
            
            if name_match:
                blip_data["name"] = name_match.group(1).strip()
            if hash_match:
                blip_data["hash"] = hash_match.group(1).strip()


    @staticmethod
    def extract_image_link(item, blip_data):
        img_tag = item.find("img")
        if img_tag and "src" in img_tag.attrs:
            blip_data["image_link"] = f"https://wiki.rage.mp{img_tag['src']}"

    @staticmethod
    def extract_id_from_figcaption(item, blip_data):
        figcaption = item.find("figcaption")
        if figcaption:
            id_match = re.search(r"ID:\s*(\d+)", figcaption.get_text())
            if id_match:
                blip_data["id"] = int(id_match.group(1))

    @staticmethod
    def extract_image_link_from_figure(item, blip_data):
        img_tag = item.find("img")
        if img_tag and "src" in img_tag.attrs:
            blip_data["image_link"] = f"https://wiki.rage.mp{img_tag['src']}"

    def import_data(self):
        soup = BeautifulSoup(get_html_content(f"html_and_json_sources/{self.model_name}.html"), "html.parser")
        blips = []

        # Try gallery format first (blip_colors or ped_models)
        gallery_items = soup.find_all("li", class_="gallerybox")
        
        if gallery_items:
            # Check if it's ped_models format (has name and hash)
            first_item = gallery_items[0]
            gallerytext = first_item.find("div", class_="gallerytext")
            
            if gallerytext and "Name:" in gallerytext.get_text():
                # ped_models format
                for item in gallery_items:
                    blip_data = {}
                    Importer.extract_name_and_hash(item, blip_data)
                    Importer.extract_image_link(item, blip_data)
                    if "name" in blip_data and "hash" in blip_data and "image_link" in blip_data:
                        blips.append(blip_data)
            else:
                # blip_colors format (with ID)
                for item in gallery_items:
                    blip_data = {}
                    Importer.extract_id(item, blip_data)
                    Importer.extract_image_link(item, blip_data)
                    if "id" in blip_data and "image_link" in blip_data:
                        blips.append(blip_data)
        else:
            # Figure format (markers)
            list_items = soup.find_all("li", style=lambda value: value and "display: inline-block" in value)
            for item in list_items:
                blip_data = {}
                Importer.extract_id_from_figcaption(item, blip_data)
                Importer.extract_image_link_from_figure(item, blip_data)
                if "id" in blip_data and "image_link" in blip_data:
                    blips.append(blip_data)

        save_data_to_json(blips, f"data/{self.model_name}.json")


def import_weapons():
    with open('html_and_json_sources/weapons.json', 'r', encoding='utf-8') as f:
        weapons_by_type = json.load(f)
    result = []
    for weapon_type, weapons in weapons_by_type.items():
        for name, hash_value in weapons.items():
            result.append({
                "name": f"WEAPON_{name.upper()}",
                "type": weapon_type,
                "hash": hash_value.strip()
            })
    save_data_to_json(result, filename='data/weapons.json')
