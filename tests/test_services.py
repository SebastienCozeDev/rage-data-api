"""
This file contains unit tests for the application services.
"""

from fastapi import HTTPException
import json
import pytest
from unittest.mock import mock_open, patch

from services import get_model


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


# @patch("services.open", side_effect=FileNotFoundError)
# def test_get_model_file_not_found(mock_file):
#     """
#     Test get_model when the file is not found.
#     """
#     with pytest.raises(HTTPException) as exc:
#         get_model("unknown", {})
#     assert exc.value.status_code == 404
#     assert exc.value.detail == "No model founded"
