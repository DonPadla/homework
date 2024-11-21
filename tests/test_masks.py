import pytest

from src.masks import get_mask_account, get_masks_card_number


@pytest.mark.parametrize("card_number, mask_card_number", [
    ('1234567891011121', "1234 56** **** 1121"),
    ('1234123412341234', "1234 12** **** 1234")
])
def test_masks_card_number(card_number, mask_card_number):
    assert get_masks_card_number(card_number) == mask_card_number


@pytest.mark.parametrize("account_number, mask_account_number", [
    ('73654108430135874305', "**4305"),
    ('12341234123412341234', "**1234")
])
def test_mask_account(account_number, mask_account_number):
    assert get_mask_account(account_number) == mask_account_number
