"""
This file contains all services for the application.
"""

import json
from typing import List, Union
from fastapi import Depends, status, HTTPException
from models import BlipColor, BlipModel, Control, Marker, PedModel, Weapon


def get_model(model_name: str, filters) -> Union[List[BlipModel], List[BlipColor], List[Marker], List[PedModel], List[Weapon]]:
    """
    Get model from JSON file.
    """
    try:
        with open(f"data/{model_name}.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"error": "Model not found"}
    if filters:
        data = [model for model in data if all(key in model and model[key] == value for key, value in filters.items())]
    if len(data) <= 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No model founded")
    return data


def get_model_with_id(id: int = None):
    """
    Get a model with identifier.
    """
    filters = {}
    if id is not None:
        filters["id"] = id
    return filters


def get_model_with_name(name: str = None):
    """
    Get a model with name.
    """
    filters = {}
    if name is not None:
        filters["name"] = name
    return filters


def get_model_with_equivalent(equivalent: str = None):
    """
    Get a model with equivalent.
    """
    filters = {}
    if equivalent is not None:
        filters["equivalent"] = equivalent
    return filters


def get_model_with_hash(hash: str = None):
    """
    Get a model with hash.
    """
    filters = {}
    if hash is not None:
        filters["hash"] = hash
    return filters


def get_model_with_type(type: str = None):
    """
    Get a model with type.
    """
    filters = {}
    if type is not None:
        filters["type"] = type
    return filters


def get_blip_colors(filters = Depends(get_model_with_id)) -> List[BlipColor]:
    """
    Get filtered or not blip colors.
    """
    return get_model("blip_colors", filters)


def get_blip_models(filters = Depends(get_model_with_id)) -> List[BlipModel]:
    """
    Get filtered or not blip models.
    """
    return get_model("blip_models", filters)


def get_controls(
    id_filter = Depends(get_model_with_id),
    name_filter = Depends(get_model_with_name),
    equivalent_filter = Depends(get_model_with_equivalent),
) -> List[Control]:
    """
    Get filtered or not controls.
    """
    return get_model(
        "controls",
        {
            **id_filter,
            **name_filter,
            **equivalent_filter,
        },
    )


def get_markers(filters = Depends(get_model_with_id)) -> List[Marker]:
    """
    Get filtered or not markers.
    """
    return get_model("markers", filters)


def get_ped_models(
    name_filter = Depends(get_model_with_name),
    hash_filter = Depends(get_model_with_hash),
) -> List[PedModel]:
    """
    Get filtered or not ped models.
    """
    return get_model(
        "ped_models",
        {
            **name_filter,
            **hash_filter,
        },
    )


def get_weapons(
    name_filter = Depends(get_model_with_name),
    hash_filter = Depends(get_model_with_hash),
    type_filter = Depends(get_model_with_type),
) -> List[Weapon]:
    """
    Get filtered or not weapons.
    """
    return get_model(
        "weapons",
        {
            **name_filter,
            **hash_filter,
            **type_filter,
        },
    )
