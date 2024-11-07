def filter_by_state(list_of_dictionaries: list, state='EXECUTED') -> list:
    """ Принимает список словарей и опционально значение для ключа state, возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению """
    filter_list = []
    for states in list_of_dictionaries:
        if states.get('state') == state:
            filter_list.append(states)
    return filter_list


def sort_by_date(list_of_dictionaries: list, sort_parameter='True') -> list:
    """ Принимает список словарей и необязательный параметр, задающий порядок сортировки, возвращает новый список, отсортированный по дате """
    sorted_list = sorted(list_of_dictionaries, key=lambda x: x['date'], reverse=sort_parameter)
    return sorted_list
