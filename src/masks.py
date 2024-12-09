import logging

logger = logging.getLogger('masks')
file_handler = logging.FileHandler(
    '/home/don_padla/PycharmProjects/project_for_bank_1.2/logs/masks.log', 'w'
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_masks_card_number(card_number: str) -> str:
    logger.info('Masking the card number started.')
    """ Принимает на вход номер карты в виде числа и возвращает маску номера по правилу XXXX XX** **** XXXX """
    if len(card_number) != 16:
        logger.error('Error. Incorrect data!.')
        return """
        Incorrect data.
        Card number must consist of 16 digits.
        Try again.
        """
    else:
        mask_card_number = []
        for i in range(len(card_number)):
            if 5 < i < 12:
                mask_card_number.append('*')
            else:
                mask_card_number.append(card_number[i])
        splited_card_number = []
        for i in range(len(mask_card_number)):
            if i % 4 != 0:
                splited_card_number.append(mask_card_number[i])
            else:
                splited_card_number.append(' ')
                splited_card_number.append(mask_card_number[i])
        logger.info('The disguise is successful.')
        logger.info('Operation is completed.')
        return ''.join(splited_card_number).lstrip()


def get_mask_account(account_number: str) -> str:
    """ Принимает на вход номер счета в виде числа и возвращает маску номера по правилу **XXXX """

    logger.info('Masking the account number started.')
    if len(account_number) != 20:
        logger.error('Error. Incorrect data!')
        return """
        Incorrect data.
        Card account must consist of 20 digits.
        Try again.
        """
    else:
        logger.info('The disguise is successful.')
        str_account_number = str(account_number)
        mask_account_number = f'**{str_account_number[-4:]}'
        logger.info('Operation is completed.')
        return mask_account_number
