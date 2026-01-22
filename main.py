from typing import Union, List

from fastapi import FastAPI
import json

from import_data.importer import Importer, import_weapons
from models import BlipModels, BlipColor, Markers, PedModels, Weapons

tags_metadata = [
    {
        "name": "Models",
        "description": "Operations with GTA5 models. Retrieve various model data.",
    },
]

app = FastAPI(
    title="GTA5 Models API",
    description="An API to access GTA5 model data such as blip models, colors, markers, ped models, and weapons.",
    summary="An API for GTA5 model data retrieval.",
    version="0.1.0-alpha.2",
    openapi_tags=tags_metadata,
    docs_url="/",
    redoc_url="/redoc",
)


def read_model(model_name: str, **kwargs) -> Union[List[BlipModels], List[BlipColor], List[Markers], List[PedModels], List[Weapons]]:
    try:
        with open(f"data/{model_name}.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"error": "Model not found"}
    if kwargs:
        data = [model for model in data if all(key in model and model[key] == value for key, value in kwargs.items())]
    return data


@app.get(
    "/blip_colors",
    tags=["Models"],
    summary="Retrieve blip colors data",
    description="Fetches and returns the JSON data for blip colors models.",
)
def read_blip_colors() -> List[BlipColor]:
    return read_model("blip_colors")


@app.get(
    "/blip_models",
    tags=["Models"],
    summary="Retrieve blip models data",
    description="Fetches and returns the JSON data for blip models.",
)
def read_blip_models(id: int = None) -> List[BlipModels]:
    kwargs = {}
    if id is not None:
        kwargs["id"] = id
    return read_model("blip_models", **kwargs)

@app.get(
    "/markers",
    tags=["Models"],
    summary="Retrieve markers data",
    description="Fetches and returns the JSON data for markers.",
)
def read_markers(id: int = None) -> List[Markers]:
    kwargs = {}
    if id is not None:
        kwargs["id"] = id
    return read_model("markers", **kwargs)

@app.get(
    "/ped_models",
    tags=["Models"],
    summary="Retrieve ped models data",
    description="Fetches and returns the JSON data for ped models.",
)
def read_ped_models(name: str = None, hash: str = None) -> List[PedModels]:
    kwargs = {}
    if name is not None:
        kwargs["name"] = name
    if hash is not None:
        kwargs["hash"] = hash
    return read_model("ped_models", **kwargs)

@app.get(
    "/weapons",
    tags=["Models"],
    summary="Retrieve weapons data",
    description="Fetches and returns the JSON data for weapons models.",
)
def read_weapons(type: str = None, name: str = None, hash: str = None) -> List[Weapons]:
    kwargs = {}
    if type is not None:
        kwargs["type"] = type
    if name is not None:
        kwargs["name"] = name
    if hash is not None:
        kwargs["hash"] = hash
    return read_model("weapons", **kwargs)


if __name__ == "__main__":
    print("Importing data...")
    Importer("blip_models").import_data()
    Importer("blip_colors").import_data()
    Importer("markers").import_data()
    Importer("ped_models").import_data()
    import_weapons()

