def filter_by_state(list_of_dictionaries: list, state: str = 'EXECUTED') -> list:
    """ Принимает список словарей и опционально значение для ключа state, возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению """
    filtered_list = []
    for dictionari in list_of_dictionaries:
        if dictionari.get('state') == state:
            filtered_list.append(dictionari)
    return filtered_list


def sort_by_date(list_of_dictionaries: list, sort_parameter: bool = True) -> list:
    """ Принимает список словарей и необязательный параметр, задающий порядок сортировки,
    возвращает новый список, отсортированный по дате """
    sorted_list = sorted(list_of_dictionaries, key=lambda x: x['date'], reverse=sort_parameter)
    return sorted_list
