import pandas as pd
from src.logging_set import logger
import csv


def get_open_csv_file(imported_file):
    """ Принимает на вход путь до csv-файла, возвращает данные о финансовых транзакциях """

    logger.info(f'{imported_file}: opening attempt.')
    list_transaction = []

    try:
        with open(imported_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            logger.info(f'{imported_file}: ok.')
            for row in reader:
                list_transaction.append(row)
        logger.info('Operation is completed.')
        return list_transaction

    except Exception:
        logger.error('File cannot be opened.')
        return list_transaction


def get_open_xlsx_file(imported_file):
    """ Принимает на вход путь до xlsx-файла, возвращает данные о финансовых транзакциях """

    logger.info(f'{imported_file}: opening attempt.')

    try:
        reader = pd.read_excel(imported_file)
        list_transaction = reader.to_dict(orient='records')
        logger.info(f'{imported_file}: ok.')
        logger.info('Operation is completed.')
        return list_transaction

    except Exception:
        logger.error('File cannot be opened.')
        return []
