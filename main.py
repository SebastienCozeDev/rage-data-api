from typing import List

from fastapi import Depends
from fastapi import FastAPI

from import_data.importer import Importer, import_weapons
from models import BlipModels, BlipColor, Markers, PedModels, Weapons
from services import get_blip_colors, get_blip_models, get_markers, get_model, get_ped_models, get_weapons


tags_metadata = [
    {
        "name": "Models",
        "description": "Operations with GTA5 models. Retrieve various model data.",
    },
]

app = FastAPI(
    title="RAGE Data API",
    description="An API to access RAGE data such as blip models, colors, markers, ped models, and weapons.",
    summary="An API for RAGE data retrieval.",
    version="0.1.0-beta.2",
    openapi_tags=tags_metadata,
    docs_url="/",
    redoc_url="/redoc",
)


@app.get(
    "/blip_colors",
    tags=["Models"],
    summary="Retrieve blip colors data",
    description="Fetches and returns the JSON data for blip colors models.",
)
def read_blip_colors(result = Depends(get_blip_colors)) -> List[BlipColor]:
    return result


@app.get(
    "/blip_models",
    tags=["Models"],
    summary="Retrieve blip models data",
    description="Fetches and returns the JSON data for blip models.",
)
def read_blip_models(result = Depends(get_blip_models)) -> List[BlipModels]:
    return result


@app.get(
    "/markers",
    tags=["Models"],
    summary="Retrieve markers data",
    description="Fetches and returns the JSON data for markers.",
)
def read_markers(result = Depends(get_markers)) -> List[Markers]:
    return result


@app.get(
    "/ped_models",
    tags=["Models"],
    summary="Retrieve ped models data",
    description="Fetches and returns the JSON data for ped models.",
)
def read_ped_models(result = Depends(get_ped_models)) -> List[PedModels]:
    return result


@app.get(
    "/weapons",
    tags=["Models"],
    summary="Retrieve weapons data",
    description="Fetches and returns the JSON data for weapons models.",
)
def read_weapons(result = Depends(get_weapons)) -> List[Weapons]:
    return result


@app.get(
    "/health",
    tags=["Health"],
    summary="Retrieve the server status",
    description="Fetches and returns the JSON data for server status",
)
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    print("Importing data...")
    Importer("blip_models").import_data()
    Importer("blip_colors").import_data()
    Importer("markers").import_data()
    Importer("ped_models").import_data()
    import_weapons()
