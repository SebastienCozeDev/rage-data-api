"""
This file is the main file of the application. It is used to run the application or create the JSON data files.
"""


from typing import List

from fastapi import Depends
from fastapi import FastAPI

from import_data.importer import Importer, import_weapons
from models import BlipModel, BlipColor, Control, Marker, PedModel, Weapon
from services import get_blip_colors, get_blip_models, get_controls, get_markers, get_ped_models, get_weapons


tags_metadata = [
    {
        "name": "GTA5",
        "description": "Operations with Grand Theft Auto V models. Retrieve various model data.",
    },
    {
        "name": "Health",
        "description": "Operations related to server health and status checks.",
    },
]

with open("README.md", "r", encoding="utf-8") as f:
    readme_content = f.read()
    lines = readme_content.split('\n')
    roadmap_index = next((i for i, line in enumerate(lines) if "🎯 Roadmap" in line), 0)
    readme_content = '\n'.join(lines[roadmap_index:])

app = FastAPI(
    title="⚙️ RAGE Data API",
    summary="RAGE Data API allows you to retrieve useful information from video games using the RAGE game engine. This information helps, in particular, mod developers to simplify their research.",
    description=readme_content,
    version="0.1.2",
    openapi_tags=tags_metadata,
    docs_url="/",
    redoc_url="/redoc",
)


@app.get(
    "/blip_colors",
    tags=["GTA5"],
    summary="Retrieve blip colors data",
    description="Fetches and returns the JSON data for blip colors models.",
)
def read_blip_colors(result = Depends(get_blip_colors)) -> List[BlipColor]:
    """
    Endpoint to get the blip colors.
    """
    return result


@app.get(
    "/blip_models",
    tags=["GTA5"],
    summary="Retrieve blip models data",
    description="Fetches and returns the JSON data for blip models.",
)
def read_blip_models(result = Depends(get_blip_models)) -> List[BlipModel]:
    """
    Endpoint to get the blip models.
    """
    return result


@app.get(
    "/controls",
    tags=["GTA5"],
    summary="Retrieve controls data",
    description="Fetches and returns the JSON data for controls.",
)
def read_controls(result = Depends(get_controls)) -> List[Control]:
    """
    Endpoint to get the controls.
    """
    return result


@app.get(
    "/markers",
    tags=["GTA5"],
    summary="Retrieve markers data",
    description="Fetches and returns the JSON data for markers.",
)
def read_markers(result = Depends(get_markers)) -> List[Marker]:
    """
    Endpoint to get the markers.
    """
    return result


@app.get(
    "/ped_models",
    tags=["GTA5"],
    summary="Retrieve ped models data",
    description="Fetches and returns the JSON data for ped models.",
)
def read_ped_models(result = Depends(get_ped_models)) -> List[PedModel]:
    """
    Endpoint to get the ped models.
    """
    return result


@app.get(
    "/weapons",
    tags=["GTA5"],
    summary="Retrieve weapons data",
    description="Fetches and returns the JSON data for weapons models.",
)
def read_weapons(result = Depends(get_weapons)) -> List[Weapon]:
    """
    Endpoint to get the weapons.
    """
    return result


@app.get(
    "/health",
    tags=["Health"],
    summary="Retrieve the server status",
    description="Fetches and returns the JSON data for server status",
)
def health():
    """
    Endpoint to get the server status.
    """
    return {"status": "ok"}


if __name__ == "__main__":
    print("Importing data...")
    Importer("blip_models").import_data()
    Importer("blip_colors").import_data()
    Importer("markers").import_data()
    Importer("ped_models").import_data()
    import_weapons()
