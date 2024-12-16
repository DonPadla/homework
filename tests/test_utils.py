from unittest.mock import mock_open, patch

from src.utils import get_convert_currency, get_open_operation_file


@patch("builtins.open", new_callable=mock_open, read_data='{"test_mock": {"mock": "ok", "open": "yes"}}')
def test_get_open_operation_file(mock_file):
    expected_result = {'test_mock': {'mock': 'ok', 'open': 'yes'}}
    result = get_open_operation_file('test_file')
    assert result == expected_result


def test_error_open_operations_file():
    file = "/test_error/not_found"
    assert get_open_operation_file(file) == []
    assert get_open_operation_file(None) == []


@patch('requests.request')
def test_convert_currency(mock_get):
    mock_get.return_value.json.return_value = {
        "query": {"amount": 100, "from": "USD", "to": "RUB"},
        "result": 3642.723,
    }
    assert get_convert_currency(
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    ) == 3642.723
