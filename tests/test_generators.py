import pytest

from src.generators import card_number_generator


def test_filter_by_currency(transaction_list, usd_currency, rub_currency):
    usd_result = list(
        transaction for transaction in transaction_list if transaction['operationAmount']['currency']['code'] == 'USD'
    )
    rub_result = list(
        transaction for transaction in transaction_list if transaction['operationAmount']['currency']['code'] == 'RUB'
    )
    assert usd_result == usd_currency
    assert rub_result == rub_currency


def test_transaction_descriptions(transaction_list):
    num = (transaction['description'] for transaction in transaction_list)
    assert next(num) == "Перевод организации"
    assert next(num) == "Перевод со счета на счет"
    assert next(num) == "Перевод со счета на счет"
    assert next(num) == "Перевод с карты на карту"


@pytest.mark.parametrize('start, stop, number', [
    (1, 5, [
        '0000 0000 0000 0001',
        '0000 0000 0000 0002',
        '0000 0000 0000 0003',
        '0000 0000 0000 0004',
        '0000 0000 0000 0005'
    ]),
    (9999999999999994, 9999999999999999, [
        '9999 9999 9999 9994',
        '9999 9999 9999 9995',
        '9999 9999 9999 9996',
        '9999 9999 9999 9997',
        '9999 9999 9999 9998',
        '9999 9999 9999 9999',
    ]),
    (5, 1, [])
]
)
def test_card_number_generator(start, stop, number):
    num = list(x for x in card_number_generator(start, stop))
    assert num == number
