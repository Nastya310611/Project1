import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.mark.parametrize(
    'currency, expected',
    [
        ('USD', [{
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
         {
             "id": 142264268,
             "state": "EXECUTED",
             "date": "2019-04-04T23:20:05.206878",
             "operationAmount": {
                 "amount": "79114.93",
                 "currency": {
                     "name": "USD",
                     "code": "USD"
                 }
             },
             "description": "Перевод со счета на счет",
             "from": "Счет 19708645243227258542",
             "to": "Счет 75651667383060284188"
         },
         {
             "id": 895315941,
             "state": "EXECUTED",
             "date": "2018-08-19T04:27:37.904916",
             "operationAmount": {
                 "amount": "56883.54",
                 "currency": {
                     "name": "USD",
                     "code": "USD"
                 }
             },
             "description": "Перевод с карты на карту",
             "from": "Visa Classic 6831982476737658",
             "to": "Visa Platinum 8990922113665229"
         }]),
         ('EUR', []), #Транзакции в заданной валюте отсутствуют
    ])
def test_filter_by_currency(transactions: list, currency : str, expected: list):
    """Проверка функции при наличии списка транзакций"""
    assert list(filter_by_currency(transactions, currency)) == expected


def test_filter_by_currency_empty_list():
    """Проверка функции при отсутствии списка транзакций"""
    empty_transactions = []
    result = filter_by_currency(empty_transactions, 'RUB')
    with pytest.raises(StopIteration):
        next(result)


def test_transaction_descriptions(transactions):
    """Проверка функции при наличии description"""
    desc_generator = transaction_descriptions(transactions)
    first_desc = next(desc_generator)
    assert first_desc == 'Перевод организации'
    second_desc = next(desc_generator)
    assert second_desc == 'Перевод со счета на счет'


def test_transaction_descriptions_empty_list():
    """Проверка функции при отсутствии списка транзакций"""
    empty_transactions = []
    result = transaction_descriptions(empty_transactions)
    with pytest.raises(StopIteration):
        next(result)


@pytest.mark.parametrize(
    'start, stop, expected',
    [
        (1, 5, ['0000 0000 0000 0001', # Корректный ввод диапазона
                '0000 0000 0000 0002',
                '0000 0000 0000 0003',
                '0000 0000 0000 0004',
                '0000 0000 0000 0005',]),

        (23, 23, ['0000 0000 0000 0023',]), # Ввод одинаковых чисел
        (6, 3, []), # Начало списка больше конца

        (20876, 20879, ['0000 0000 0002 0876', # Диапазон из чисел, больше 4 символов
                        '0000 0000 0002 0877',
                        '0000 0000 0002 0878',
                        '0000 0000 0002 0879']),
    ]
)
def test_card_number_generator(start, stop, expected):
    assert list(card_number_generator(start, stop)) == expected