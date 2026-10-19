def filter_by_currency(transactions: list, currency: str) -> iter:
    """Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    return (transaction for transaction in transactions
            if transaction['operationAmount']['currency']['code'] == currency)


def transaction_descriptions(transactions: list) -> iter:
    """Генератор ринимает список словарей с транзакциями и возвращает
    описание каждой операции по очереди """
    return (transaction.get('description', 'Описание отсутствует') for transaction in transactions)