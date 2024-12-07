import json
from src.external_api import get_convert_amount


def get_open_operation_file(imported_file):
    ''' Принимает на вход путь до JSON-файла, возвращает данные о финансовых транзакциях '''

    operations_list = []
    try:
        with open(imported_file, 'r') as file_json:
            operations_list = json.load(file_json)
        return operations_list

    except Exception:
        return operations_list


def get_convert_currency(transaction):
    ''' Принимает транзакцию, возвращает ее сумму '''

    if transaction['operationAmount']['currency']['code'] == 'RUB':
        return transaction['operationAmount']['amount']

    elif transaction['operationAmount']['currency']['code'] != 'RUB':
        convert_currency = get_convert_amount(
            transaction['operationAmount']['amount'], transaction['operationAmount']['currency']['code']
        )
        return convert_currency
