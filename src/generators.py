from src.masks import get_mask_card_number


def filter_by_currency(transactions: list, currency: str) -> iter:
    """Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    return (transaction for transaction in transactions
            if transaction['operationAmount']['currency']['code'] == currency)


def transaction_descriptions(transactions: list) -> iter:
    """Генератор ринимает список словарей с транзакциями и возвращает
    описание каждой операции по очереди """
    return (transaction.get('description', 'Описание отсутствует') for transaction in transactions)


def card_number_generator(start: int, stop: int) -> iter:
    """Генератор который выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX, где X — цифра номера карты"""
    for number in range(start, stop + 1):
        card_str = str(number).zfill(16)
        formated_card = get_mask_card_number(card_str)
        yield formated_card