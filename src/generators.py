from typing import Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator:
    """Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    return (
        transaction for transaction in transactions if transaction["operationAmount"]["currency"]["code"] == currency
    )


def transaction_descriptions(transactions: list) -> Iterator:
    """Генератор ринимает список словарей с транзакциями и возвращает
    описание каждой операции по очереди"""
    return (transaction.get("description", "Описание отсутствует") for transaction in transactions)


def card_number_generator(start: int, stop: int) -> Iterator:
    """Генератор который выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX, где X — цифра номера карты"""
    for number in range(start, stop + 1):
        card_number = str(number).zfill(16)
        formated_card = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formated_card
