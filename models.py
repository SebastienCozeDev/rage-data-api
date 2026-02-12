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
        example=1,
    )
    image_link: str = Field(
        description="Link to an image of the model",
        example="https://example.com/model_image.png"
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
class PedModel:
    """
    Ped model model.
    """
    name: str = Field(
        description="Name of the ped model",
        example="player_zero"
    )
    hash: str = Field(
        description="Hexadecimal hash of the ped model",
        example="0x92A27487"
    )
    image_link: str = Field(
        description="Link to an image of the ped model",
        example="https://example.com/ped_image.png"
    )


@dataclass
class Weapon:
    """
    Weapon model.
    """
    name: str = Field(
        description="Name of the weapon",
        example="WEAPON_DAGGER",
    )
    hash: str = Field(
        description="Hexadecimal hash of the weapon",
        example="0x92A27487",
    )
    type: str = Field(
        description="Type of weapon (melee, handguns, smg, shotguns, assault rifles, machine guns, sniper rifles, heavy weapons, throwables, misc)",
        example="melee",
    )
