from unittest.mock import patch
from src.external_api import get_convert_amount


@patch("requests.request")
def test_get_convert_amount(mock_get):
    mock_get.return_value.json.return_value = {
        "query": {"amount": 100, "from": "USD", "to": "RUB"},
        "result": 3642.723,
    }
    assert get_convert_amount(100, 'USD') == 3642.723
