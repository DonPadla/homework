def filter_by_state(list_of_dictionaries: list, state='EXECUTED') -> list:
    """ принимает список словарей и опционально значение для ключа state, возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению"""
    filter_list = []
    for states in list_of_dictionaries:
        if states.get('state') == state:
            filter_list.append(states)
    return filter_list
