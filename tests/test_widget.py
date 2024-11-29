import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("card_data, mask_data", [
    ('Visa Platinum 7000792289606361', "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305")
])
def test_card_data(card_data, mask_data):
    assert mask_account_card(card_data) == mask_data


@pytest.mark.parametrize("date, correct_date", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("1994-02-14T19:32:41.373418", "14.02.1994"),
    ("0001-01-01T00:00:000000", "01.01.0001")
])
def test_date(date, correct_date):
    assert get_date(date) == correct_date
