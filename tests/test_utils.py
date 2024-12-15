from unittest.mock import patch
from src.utils import get_open_operation_file
from src.utils import get_convert_currency


def test_get_open_operation_file(data_from_oprations):
    file = "../data/operations.json"
    assert get_open_operation_file(file) == data_from_oprations


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
