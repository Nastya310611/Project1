import pytest

from src.processing import filter_by_state, sort_by_date, process_bank_search


@pytest.mark.parametrize(
    "state, expected",
    [
        ("EXECUTED", [1, 3]),
        ("CANCELED", [2, 5]),
        ("PENDING", [4]),
    ],
)
# Проверка работы функции с корректными входными данными
def test_filter_by_state(sample_transaction: list, state: str, expected: list) -> None:
    result = filter_by_state(sample_transaction, state=state)
    assert len(result) == len(expected)
    assert [item["id"] for item in result] == expected


# Проверка работы функции по умолчанию без указания state
def test_filter_by_state_default(sample_transaction: list) -> None:
    result = filter_by_state(sample_transaction)
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


# Проверка при отсутствии словарей с заданным статусом
def test_filter_by_state_no_matches(sample_transaction: list) -> None:
    result = filter_by_state(sample_transaction, state="UNKNOWN")
    assert result == []


# Проверка при вводе пустого списка
def test_filter_by_state_empty_list() -> None:
    assert filter_by_state([]) == []


# Проверка сортировки по убыванию
def test_sort_by_date_descending(sample_dates: list) -> None:
    result = sort_by_date(sample_dates, reverse=True)
    assert [item["date"] for item in result] == [
        "2024-01-03T12:00:00",
        "2024-01-03T12:00:00",
        "2024-01-02T11:00:00",
        "2024-01-01T10:00:00",
    ]


# Проверка сортировки по возрастанию
def test_sort_by_date_ascending(sample_dates: list) -> None:
    result = sort_by_date(sample_dates, reverse=False)
    assert [item["date"] for item in result] == [
        "2024-01-01T10:00:00",
        "2024-01-02T11:00:00",
        "2024-01-03T12:00:00",
        "2024-01-03T12:00:00",
    ]


# Проверка корректности при одинаковых датах
def test_sort_by_date_same_dates(sample_dates: list) -> None:
    result = sort_by_date(sample_dates, reverse=True)
    assert result[0]["id"] == 1
    assert result[1]["id"] == 4


# Проверка работы с некорректными данными
def test_sort_by_date_invalid_formats() -> None:
    data = [
        {"id": 1, "date": "01.01.2024"},
        {"id": 2, "date": "2024-01-02"},
    ]
    result = sort_by_date(data)
    assert len(result) == 2


# Тест работы функции поиска заданной строки в операциях: корректный ввод, наличие строки
def test_process_bank_search_correct(transactions: list[dict]) -> None:
    search = 'организации'
    expected = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        }
    ]
    result = process_bank_search(transactions, search)
    assert result == expected


# Тест работы функции поиска заданной строки в операциях: операции с заданным словом отсутствуют
def test_process_bank_search_empty_list(transactions: list[dict]) -> None:
    search = 'банку'
    expected = []
    result = process_bank_search(transactions, search)
    assert result == expected


# Тест работы функции поиска заданной строки в операциях: ввод с верхним регистром
def test_process_bank_search_uppercase(transactions: list[dict]) -> None:
    search = 'Организации'
    expected = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        }
    ]
    result = process_bank_search(transactions, search)
    assert result == expected


# Тест работы функции поиска заданной строки в операциях: ввод пустой строки
def test_process_bank_search_empty_str(transactions: list[dict]) -> None:
    search = ''
    expected = [
    {    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
    ]
    result = process_bank_search(transactions, search)
    assert result == expected


