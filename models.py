"""
This file contains all models for the application.
"""


from pydantic import Field
from pydantic.dataclasses import dataclass


@dataclass
class IdAndImageLink:
    """
    Template model class which use id and image link.
    """
    id: int = Field(
        description="Unique identifier for the model",
        json_schema_extra={"example": 1},
    )
    image_link: str = Field(
        description="Link to an image of the model",
        json_schema_extra={"example": "https://example.com/model_image.png"},
    )



@dataclass
class BlipColor(IdAndImageLink):
    """
    Blip color model.
    """


@dataclass
class BlipModel(IdAndImageLink):
    """
    Blip model model.
    """


@dataclass
class Marker(IdAndImageLink):
    """
    Marker model.
    """


@dataclass
class Control:
    """
    Control model.
    """
    id: int = Field(
        description="Unique identifier for the control",
        json_schema_extra={"example": 235},
    )
    name: str = Field(
        description="Name of the control",
        json_schema_extra={"example": "INPUT_JUMP"},
    )
    equivalent: str = Field(
        description="Equivalent control in keyboard or mouse button",
        json_schema_extra={"example": "Space Key"},
    )


@dataclass
class PedModel:
    """
    Ped model model.
    """
    name: str = Field(
        description="Name of the ped model",
    )
    hash: str = Field(
        description="Hexadecimal hash of the ped model",
        json_schema_extra={"example": "0x92A27487"},
    )
    image_link: str = Field(
        description="Link to an image of the ped model",
        json_schema_extra={"example": "https://example.com/ped_image.png"},
    )


@dataclass
class Weapon:
    """
    Weapon model.
    """
    name: str = Field(
        description="Name of the weapon",
        json_schema_extra={"example": "WEAPON_DAGGER"},
    )
    hash: str = Field(
        description="Hexadecimal hash of the weapon",
        json_schema_extra={"example": "0x92A27487"},
    )
    type: str = Field(
        description="Type of weapon (melee, handguns, smg, shotguns, assault rifles, machine guns, sniper rifles, heavy weapons, throwables, misc)",
        json_schema_extra={"example": "melee"},
    )
