from collections import Counter

from src.search import get_count_transaction_by_category, get_search_transactions


def test_search_transactions(transactions, usd_currency):
    assert get_search_transactions(transactions,  "USD") == usd_currency


def test_count_transaction_by_category(transactions):
    assert get_count_transaction_by_category(
        transactions, ['Перевод организации', 'Перевод с карты на карту']
    ) == Counter({'Перевод организации': 2, 'Перевод с карты на карту': 1})


def test_up_low_count_transaction(transactions):
    assert (
            get_count_transaction_by_category(transactions, ['перевод Организации'])
            == Counter({'Перевод организации': 2})
    )


def test_not_list_count_transaction(transactions):
    assert get_count_transaction_by_category(
        transactions, 'Перевод организации'
                                             ) == ' Для успешного поиска, передайте категории списком. '
