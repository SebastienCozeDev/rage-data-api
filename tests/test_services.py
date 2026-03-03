"""
This file contains unit tests for the application services.
"""

from fastapi import HTTPException
import json
import pytest
from unittest.mock import mock_open, patch

from services import (
    get_controls,
    get_model,
    get_model_with_equivalent,
    get_model_with_id,
    get_model_with_name,
    get_model_with_hash,
    get_model_with_type,
    get_ped_models,
    get_blip_colors,
    get_blip_models,
    get_markers,
    get_weapons,
)


SAMPLE_DATA = [
    {"id": 1, "name": "A", "type": "melee"},
    {"id": 2, "name": "B", "type": "rifle"},
]


def _mock_file(data):
    """
    Mock the open function to return the provided data as a file-like object.
    """
    return mock_open(read_data=json.dumps(data))


@patch("services.open", new_callable=lambda: _mock_file(SAMPLE_DATA))
def test_get_model_no_filters(mock_file):
    """
    Test get_model without filters.
    """
    result = get_model("weapons", {})
    assert result == SAMPLE_DATA


@patch("services.open", new_callable=lambda: _mock_file(SAMPLE_DATA))
def test_get_model_with_id_filter(mock_file):
    """
    Test get_model with id filter.
    """
    result = get_model("weapons", {"id": 1})
    assert result == [{"id": 1, "name": "A", "type": "melee"}]


@patch("services.open", new_callable=lambda: _mock_file(SAMPLE_DATA))
def test_get_model_with_type_filter(mock_file):
    """
    Test get_model with type filter.
    """
    result = get_model("weapons", {"type": "rifle"})
    assert result == [{"id": 2, "name": "B", "type": "rifle"}]


@patch("services.open", side_effect=FileNotFoundError)
def test_get_model_file_not_found(mock_file):
    """
    Test get_model when the file is not found.
    """
    with pytest.raises(HTTPException) as exc:
        get_model("weapons", {"id": 999})
    assert exc.value.status_code == 404
    assert exc.value.detail == "No model founded"


def test_get_model_with_id():
    """
    Test get_model_with_id function.
    """
    assert get_model_with_id(1) == {"id": 1}
    assert get_model_with_id() == {}


def test_get_model_with_name():
    """
    Test get_model_with_name function.
    """
    assert get_model_with_name("A") == {"name": "A"}
    assert get_model_with_name() == {}


def test_get_model_with_hash():
    """
    Test get_model_with_hash function.
    """
    assert get_model_with_hash("0x123") == {"hash": "0x123"}
    assert get_model_with_hash() == {}


def test_get_model_with_type():
    """
    Test get_model_with_type function.
    """
    assert get_model_with_type("melee") == {"type": "melee"}
    assert get_model_with_type() == {}


@patch("services.get_model")
def test_get_ped_models(mock_get_model):
    name_filter = get_model_with_name("A")
    hash_filter = get_model_with_hash("0x123")
    mock_get_model.return_value = [{"name": "A", "hash": "0x123"}]
    result = get_ped_models(name_filter=name_filter, hash_filter=hash_filter)
    mock_get_model.assert_called_once_with(
        "ped_models",
        {"name": "A", "hash": "0x123"}
    )
    assert isinstance(result, list)


@patch("services.get_model")
def test_get_blip_colors(mock_get_model):
    filters = get_model_with_id(1)
    mock_get_model.return_value = [{"id": 1}]
    result = get_blip_colors(filters)
    mock_get_model.assert_called_once_with("blip_colors", filters)
    assert isinstance(result, list)


@patch("services.get_model")
def test_get_blip_models(mock_get_model):
    filters = get_model_with_id(1)
    mock_get_model.return_value = [{"id": 1}]
    result = get_blip_models(filters)
    mock_get_model.assert_called_once_with("blip_models", filters)
    assert isinstance(result, list)


@patch("services.get_model")
def test_get_controls(mock_get_model):
    id_filter = get_model_with_id(235)
    name_filter = get_model_with_name("INPUT_JUMP")
    equivalent_filter = get_model_with_equivalent("Space Key")
    mock_get_model.return_value = [{"id": 235, "name": "INPUT_JUMP", "equivalent": "Space Key"}]
    result = get_controls(
        id_filter=id_filter,
        name_filter=name_filter,
        equivalent_filter=equivalent_filter
    )
    mock_get_model.assert_called_once_with(
        "controls",
        {
            **id_filter,
            **name_filter,
            **equivalent_filter,
        }
    )
    assert isinstance(result, list)


@patch("services.get_model")
def test_get_markers(mock_get_model):
    filters = get_model_with_id(1)
    mock_get_model.return_value = [{"id": 1}]
    result = get_markers(filters)
    mock_get_model.assert_called_once_with("markers", filters)
    assert isinstance(result, list)


@patch("services.get_model")
def test_get_weapons(mock_get_model):
    name_filter = get_model_with_name("A")
    hash_filter = get_model_with_hash("0x123")
    type_filter = get_model_with_type("melee")
    mock_get_model.return_value = [{"name": "A", "type": "melee"}]
    result = get_weapons(
        name_filter=name_filter,
        hash_filter=hash_filter,
        type_filter=type_filter
    )
    mock_get_model.assert_called_once_with(
        "weapons",
        {
            **name_filter,
            **hash_filter,
            **type_filter
        }
    )
    assert isinstance(result, list)
