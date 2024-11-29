import pytest

from src.masks import get_mask_account, get_masks_card_number


@pytest.mark.parametrize("card_number, mask_card_number", [
    (1234567891011121, "1234 56** **** 1121"),
    (1234123412341234, "1234 12** **** 1234")
])
def test_masks_card_number(card_number, mask_card_number):
    assert get_masks_card_number(card_number) == mask_card_number


def test_zero_mask_card_number():
    with pytest.raises(AssertionError):
        assert get_masks_card_number(0000000000000000) == "0000 00** **** 0000"


@pytest.mark.parametrize("account_number, mask_account_number", [
    (73654108430135874305, "**4305"),
    (12341234123412341234, "**1234")
])
def test_mask_account(account_number, mask_account_number):
    assert get_mask_account(account_number) == mask_account_number


def test_zero_account():
    with pytest.raises(AssertionError):
        assert get_mask_account(00000000000000000000) == "**0000"
