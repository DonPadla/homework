from unittest.mock import mock_open, patch

import pandas as pd

from src.datareaders import get_open_csv_file, get_open_xlsx_file


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='id,state,date\n41428829,EXECUTED,2019-07-03T18:35:29.512364\n'
)
def test_read_csv_file(file):
    result = [{'id,state,date': '41428829,EXECUTED,2019-07-03T18:35:29.512364'}]
    assert result == get_open_csv_file('test_file')


def test_error_read_csv_file():
    result = []
    assert result == get_open_csv_file(None)


@patch("pandas.read_excel")
def test_open_xlsx_file(mock_read_excel):
    mock_read_excel.return_value = pd.DataFrame([
        {
            'id': 650703.0,
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'amount': 16210.0
        }
    ])

    assert get_open_xlsx_file('test_file') == [
        {
            'id': 650703.0,
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'amount': 16210.0
        }
    ]


def test_error_open_xlsx_file():
    result = []
    assert result == get_open_xlsx_file(None)
