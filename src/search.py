import re
from collections import Counter

from src.logging_set import logger


def get_search_transactions(transaction_list, search_bar):
    """ Функция для поиска в списке словарей операций по заданной строке """

    pattern = re.compile(rf'{search_bar}')
    transaction_of_matches = []
    logger.info('Search start.')

    for transaction in transaction_list:
        transaction_str = str(transaction)
        match = re.search(pattern, transaction_str)

        if match:
            transaction_of_matches.append(transaction)
            logger.info('Operation is completed.')

    return transaction_of_matches


def get_count_transaction_by_category(transaction_list, categories):
    """ Функция для подсчета количества банковских операций определенного типа возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории. """

    counted = Counter()

    for transaction in transaction_list:
        str_desription = str(transaction['description']).lower()

        if type(categories) is list:

            for category in categories:

                if category.lower() in str_desription:
                    counted[transaction['description']] += 1

        else:
            logger.error('Data error.')
            counted = ' Для успешного поиска, передайте категории списком. '
        logger.info('Operation is completed.')

    return counted
