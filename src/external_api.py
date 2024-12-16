import os

import requests
from dotenv import load_dotenv  # ignore


def get_convert_amount(amount, currency):
    """ Принимает сумму и валюту, конвертирует сумму в RUB """

    load_dotenv()
    api_key = os.getenv("API_KEY")
    headers = {"apikey": api_key}
    payload = {}
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    response = requests.request("GET", url, headers=headers, data=payload)
    result = response.json()["result"]
    return result
