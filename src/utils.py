import json
import os.path

from src.external_api import get_convert_amount
import logging

file_adress = os.path.abspath(
    os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)), "../logs/utils.log"))
logger = logging.getLogger('utils')
file_handler = logging.FileHandler(
    file_adress, 'w'
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_open_operation_file(imported_file):
    ''' Принимает на вход путь до JSON-файла, возвращает данные о финансовых транзакциях '''

    logger.info(f'{imported_file}: opening attempt.')
    operations_list = []
    try:
        with open(imported_file, 'r') as file_json:
            operations_list = json.load(file_json)
            logger.info(f'{imported_file}: ok.')
        logger.info('Operation is completed.')
        return operations_list

    except Exception:
        logger.error('File cannot be opened.')
        return operations_list


def get_convert_currency(transaction):
    ''' Принимает транзакцию, возвращает ее сумму '''

    logger.info('Data transmission.')
    if transaction['operationAmount']['currency']['code'] == 'RUB':
        logger.info('No conversion is required. Calculation.')
        logger.info('Operation is completed.')
        return transaction['operationAmount']['amount']

    elif transaction['operationAmount']['currency']['code'] != 'RUB':
        logger.info('Conversion required.')
        convert_currency = get_convert_amount(
            transaction['operationAmount']['amount'], transaction['operationAmount']['currency']['code']
        )
        logger.info('Calculation.')
        logger.info('Operation is completed.')
        return convert_currency
