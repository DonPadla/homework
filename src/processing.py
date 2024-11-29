from typing import Union


def filter_by_state(list_of_dictionaries: list, state: str = 'EXECUTED') -> Union[list, str]:
    """ Принимает список словарей и опционально значение для ключа state, возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению """
    if state != 'EXECUTED' and state != 'CANCELED':
        return '''
        Invalid value.
        Enter "EXECUTED" or "CANCELED"
        '''
    else:
        filtered_list = []
        for dictionary in list_of_dictionaries:
            if dictionary.get('state') == state:
                filtered_list.append(dictionary)
        return filtered_list


def sort_by_date(list_of_dictionaries: list, sort_parameter: bool = True) -> list:
    """ Принимает список словарей и необязательный параметр, задающий порядок сортировки,
    возвращает новый список, отсортированный по дате """
    sorted_list = sorted(list_of_dictionaries, key=lambda x: x['date'], reverse=sort_parameter)
    return sorted_list
