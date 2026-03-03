"""
This file contains unit tests for the application models.
"""


from models import Control, IdAndImageLink, BlipColor, PedModel


def test_id_and_image_link_creation():
    """
    Test the IdAndImageLink creation.
    """
    obj = IdAndImageLink(id=42, image_link="https:/example.com/foo.png")
    assert obj.id == 42
    assert obj.image_link == "https:/example.com/foo.png"


def test_blip_color_inherits_id_and_image_link():
    """
    Test the BlipColor creation.
    """
    obj = BlipColor(id=1, image_link="https:/example.com/blip.png")
    assert isinstance(obj, IdAndImageLink)
    assert obj.id == 1
    assert obj.image_link == "https:/example.com/blip.png"


def test_ped_model_creation():
    """
    Test the PedModel creation.
    """
    ped = PedModel(
        name="player_zero",
        hash="0x92A27487",
        image_link="https://example.com/ped.png",
    )
    assert ped.name == "player_zero"
    assert ped.hash == "0x92A27487"
    assert ped.image_link == "https://example.com/ped.png"


def test_control_creation():
    """
    Test the Control creation.
    """
    control = Control(id=235, name="INPUT_JUMP", equivalent="Space Key")
    assert control.id == 235
    assert control.name == "INPUT_JUMP"
    assert control.equivalent == "Space Key"
