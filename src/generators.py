def filter_by_currency(transactions: list, currency: str) -> iter:
    """Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    return (transaction for transaction in transactions
            if transaction['operationAmount']['currency']['code'] == currency)
