import masks

def mask_account_card(incoming_data: str) -> str:
    """ Принимает строку с типом и номером карты или счета. Возвращает строку с замаскированным номером """
    numbers = ''
    letters = ''
    for symbol in incoming_data:
        if symbol.isdigit():
            numbers += symbol
        else:
            letters += symbol
    if len(numbers) == 16:
        masks_numbers = masks.get_masks_card_number(numbers)
    elif len(numbers) == 20:
        masks_numbers = masks.get_mask_account(numbers)
    return letters + masks_numbers


def get_date(incoming_date: str) -> str:
    """ Принимает строку с датой и возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
    date = {}
    date_list = incoming_date[:10].split('-')
    return f'{date_list[2]}.{date_list[1]}.{date_list[0]}'
