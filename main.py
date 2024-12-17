from src.datareaders import get_open_csv_file, get_open_xlsx_file
from src.logging_set import logger
from src.processing import filter_by_state, sort_by_date
from src.search import get_search_transactions
from src.utils import get_open_operation_file
from src.widget import get_date, mask_account_card


def main():
    """ Отвечает за основную логику проекта с пользователем и связывает функциональности между собой. """

    while True:
        choosing_file_format = input('''
 Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
''')
        logger.info('Start choosing format.')

        if choosing_file_format == '1':
            print('Для обработки выбран JSON-файл.')
            open_file = get_open_operation_file('data/operations.json')
            break

        elif choosing_file_format == '2':
            print('Для обработки выбран CSV-файл.')
            open_file = get_open_csv_file('data/transactions.csv')
            break

        elif choosing_file_format == '3':
            print('Для обработки выбран XLSX-файл.')
            open_file = get_open_xlsx_file('data/transactions_excel.xlsx')
            break

        else:
            logger.warning('Invalid value')
            print('!!!  Введено невалидное значение.  !!!')

    logger.info('Choosing is ok.')

    while True:
        choosing_status_of_operations = input('''Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: ''').upper()
        logger.info('Start choosing status.')

        if choosing_status_of_operations == 'EXECUTED':
            operations = filter_by_state(open_file, 'EXECUTED')
            print('Операции отфильтрованы по статусу "EXECUTED"')
            break

        elif choosing_status_of_operations == 'CANCELED':
            operations = filter_by_state(open_file, 'CANCELED')
            print('Операции отфильтрованы по статусу "CANCELED"')
            break

        elif choosing_status_of_operations == 'PENDING':
            operations = filter_by_state(open_file, 'PENDING')
            print('Операции отфильтрованы по статусу "PENDING"')
            break

        else:
            logger.warning('Invalid value.')
            print('Введено не валидное значение.')

        logger.info('Choosing is ok.')

    while True:
        choosing_date_sort = input('''Отсортировать операции по дате?
Да/Нет: ''').lower()
        logger.info('Date sort.')

        if choosing_date_sort == 'да':
            while True:
                choosing_filter_ascending = input('''Отсортировать по возрастанию или по убыванию?
По возрастанию/по убыванию: ''').lower()
                logger.info('Ascending or descending')

                if choosing_filter_ascending == 'по возрастанию':
                    operations_sort_date = sort_by_date(operations, True)
                    break

                elif choosing_filter_ascending == 'по убыванию':
                    operations_sort_date = sort_by_date(operations, False)
                    break

                else:
                    logger.warning('Invalid value')

                logger.info('Choosing is ok.')
            break

        elif choosing_date_sort == 'нет':
            operations_sort_date = operations
            break

        else:
            logger.warning('Invalid value.')

        logger.info('Choosing is ok.')

    while True:
        currency_selection = input('''Выводить только рублевые тразакции?
Да/Нет: ''').lower()
        logger.info('Currency selection.')

        if choosing_file_format == '1':
            operations_by_currency = []

            if currency_selection == 'да':
                for operation in operations_sort_date:
                    if operation['operationAmount']['currency']['code'] == 'RUB':
                        operations_by_currency.append(operation)
                break

            elif currency_selection == 'нет':
                operations_by_currency = operations_sort_date
                break

            else:
                logger.warning('Invalid value.')

        elif choosing_file_format != '1':
            operations_by_currency = []

            if currency_selection == 'да':
                for operation in operations_sort_date:
                    if operation['currency_code'] == 'RUB':
                        operations_by_currency.append(operation)
                break

            elif currency_selection == 'нет':
                operations_by_currency = operations_sort_date
                break

            else:
                logger.warning('Invalid value.')

        logger.info('Selection is ok')

    while True:
        filter_by_word = input('''Отфильтровать список транзакций по определенному слову в описании?
Да/Нет: ''').lower()
        logger.info('Word selection.')

        if filter_by_word == 'да':
            word_input = input('Введите слово: ')
            final_list = get_search_transactions(operations_by_currency, word_input)
            break

        elif filter_by_word == 'нет':
            final_list = operations_by_currency
            break

        else:
            logger.warning('Invalid value.')

        logger.info('Selection is ok')

    print(f'\nВсего банковских операций в выборке: {len(list(final_list))}\n')

    if len(list(final_list)) == 0:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')

    else:
        for transaction in final_list:
            date_transaction = get_date(transaction['date'])
            description_transaction = transaction['description']
            transaction_to = mask_account_card(transaction['to'])

            if choosing_file_format == '1':
                amount_transaction_for_json = transaction['operationAmount']['amount']
                currency_transaction_for_json = transaction['operationAmount']['currency']['code']

                if transaction.get('from'):
                    transaction_from = mask_account_card(transaction['from'])
                    print(f'''{date_transaction} {description_transaction}
{transaction_from} -> {transaction_to}
Сумма: {amount_transaction_for_json} {currency_transaction_for_json}
    ''')

                else:
                    print(f'''{date_transaction} {description_transaction}
{transaction_to}
Сумма: {amount_transaction_for_json} {currency_transaction_for_json}
    ''')

            elif choosing_file_format == '2':
                amount_transaction_for_csv = transaction['amount']
                currency_transaction_for_csv = transaction['currency_code']

                if transaction.get('from'):
                    transaction_from = mask_account_card(transaction['from'])
                    print(f'''{date_transaction} {description_transaction}
{transaction_from} -> {transaction_to}
Сумма: {amount_transaction_for_csv} {currency_transaction_for_csv}
                ''')

                else:
                    print(f'''{date_transaction} {description_transaction}
{transaction_to}
Сумма: {amount_transaction_for_csv} {currency_transaction_for_csv}
                ''')

            elif choosing_file_format == '3':
                amount_transaction_for_csv = transaction['amount']
                currency_transaction_for_csv = transaction['currency_code']

                if transaction['description'] != 'Открытие вклада':
                    transaction_from = mask_account_card(transaction['from'])
                    print(f'''{date_transaction} {description_transaction}
{transaction_from} -> {transaction_to}
Сумма: {amount_transaction_for_csv} {currency_transaction_for_csv}
                        ''')

                else:
                    print(f'''{date_transaction} {description_transaction}
{transaction_to}
Сумма: {amount_transaction_for_csv} {currency_transaction_for_csv}
                        ''')
