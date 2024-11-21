from src import masks


def mask_account_card(incoming_data: str) -> str:
    """ Принимает строку с типом и номером карты или счета. Возвращает строку с замаскированным номером """
    numbers = ''
    letters = ''
    for symbol in incoming_data:
        if symbol.isdigit():
            numbers += symbol
        elif symbol.isalpha():
            letters += symbol
        elif symbol == ' ':
            letters += symbol
        else:
            return """
            Unsupported icon.
            """
    masks_numbers = ''
    if len(numbers) == 16:
        masks_numbers = masks.get_masks_card_number(numbers)
    elif len(numbers) == 20:
        masks_numbers = masks.get_mask_account(numbers)
    else:
        return """
        Incorrect data.
        """
    return letters + masks_numbers


def get_date(incoming_date: str) -> str:
    """ Принимает строку с датой и возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
    date_list = incoming_date[:10].split('-')
    if 0 < int(date_list[2]) < 32 and 0 < int(date_list[1]) < 13:
        return f'{date_list[2]}.{date_list[1]}.{date_list[0]}'
    else:
        return '''
        Incorrect date.
        Please consult a specialist.'''
