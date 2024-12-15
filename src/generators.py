from typing import Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator[dict]:
    """ Принимает лист транзакций, возвращает итератор, который выдает транзакции по заданному параметру """

    for operation in transactions:
        if operation['operationAmount']['currency']['code'] == currency:
            yield operation


def transaction_descriptions(transactions: list) -> Iterator[str]:
    """ Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди """

    for operation in transactions:
        yield operation['description']


def card_number_generator(start: int, stop: int) -> Iterator:
    """ Генерирует числа из заданного диапазона """

    if 0 < start < stop <= 9999999999999999:
        for number in range(start, stop + 1):
            str_number = str(number)
            while len(str_number) != 16:
                str_number = '0' + str_number
            yield f'{str_number[0:4]} {str_number[4:8]} {str_number[8:12]} {str_number[12:16]}'
