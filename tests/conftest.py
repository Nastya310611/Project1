import pytest


# Фикстура для функции get_mask_card_number в masks.py
@pytest.fixture
def valid_number_card() -> str:
    return "1234567890123456"


# Фикстура для функции get_mask_card_number и get_mask_account в masks.py
@pytest.fixture
def invalid_number_1() -> str:
    return "123"


# Фикстура для функций get_mask_card_number и get_mask_account в masks.py
@pytest.fixture
def invalid_number_2() -> str:
    return "23384847739291827737736647892"


# Фикстура для функции get_mask_account
@pytest.fixture
def valid_number_account() -> str:
    return "12345678901234567654"


# Фикстура для функций get_mask_card_number и get_mask_account в masks.py
@pytest.fixture
def invalid_number_3() -> str:
    return "12356В7890123456"


# Фикстура для функций get_mask_card_number и get_mask_account в masks.py
@pytest.fixture
def invalid_number_4() -> str:
    return ""


# Фикстура с данными для тестирования функции filter_by_state в widget.py
@pytest.fixture
def sample_transaction() -> list:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T10:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-02T11:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-03T12:00:00"},
        {"id": 4, "state": "PENDING", "date": "2024-01-04T13:00:00"},
        {"id": 5, "state": "CANCELED", "date": "2024-01-05T14:00:00"},
    ]


# Фикстура с данными для тестирования функции sort_by_date в processing.py
@pytest.fixture
def sample_dates() -> list:
    return [
        {"id": 1, "date": "2024-01-03T12:00:00"},
        {"id": 2, "date": "2024-01-01T10:00:00"},
        {"id": 3, "date": "2024-01-02T11:00:00"},
        {"id": 4, "date": "2024-01-03T12:00:00"},  # Одинаковая дата с id=1
    ]


#Фикстура с данными транзакций для функции filter_by_currency в generators.py
@pytest.fixture
def transactions() -> list:
    return [
        {
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
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
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
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]