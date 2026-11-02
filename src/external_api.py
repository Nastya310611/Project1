import os

import requests
from dotenv import load_dotenv

load_dotenv(".env")


def convert_to_rub(transaction: dict) -> float:
    """Функция конвертации валюты из USD и EUR в рубли"""
    amount = transaction.get("amount", 0.0)
    currency = transaction.get("currency", "RUB")

    if currency == "RUB":
        return float(amount)

    if currency in ("USD", "EUR"):
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API key not found")

        url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"
        headers = {"apikey": api_key}

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()

            result = data.get("result")

            if result is not None:
                return float(result)
            return 0.0

        except requests.RequestException as e:
            print(f"Ошибка при запросе к API: {e}")
            raise

    return 0.0
