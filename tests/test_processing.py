import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize('state, expected', [
    ('EXECUTED', [1, 3]),
    ('CANCELED', [2, 5]),
    ('PENDING', [4]),
])
# Проверка работы функции с корректными входными данными
def test_filter_by_state(sample_transaction, state, expected):
    result = filter_by_state(sample_transaction, state=state)
    assert len(result) == len(expected)
    assert [item['id'] for item in result] == expected


# Проверка работы функции по умолчанию без указания state
def test_filter_by_state_default(sample_transaction):
    result = filter_by_state(sample_transaction)
    assert len(result) == 2
    assert all(item['state'] == 'EXECUTED' for item in result)


# Проверка при отсутствии словарей с заданным статусом
def test_filter_by_state_no_matches(sample_transaction):
    result = filter_by_state(sample_transaction, state='UNKNOWN')
    assert result == []


# Проверка при вводе пустого списка
def test_filter_by_state_empty_list():
    assert filter_by_state([]) == []


# Проверка сортировки по убыванию
def test_sort_by_date_descending(sample_dates):
    result = sort_by_date(sample_dates, reverse=True)
    assert [item['date'] for item in result] == [
        '2024-01-03T12:00:00',
        '2024-01-03T12:00:00',
        '2024-01-02T11:00:00',
        '2024-01-01T10:00:00',
    ]


# Проверка сортировки по возрастанию
def test_sort_by_date_ascending(sample_dates):
    result = sort_by_date(sample_dates, reverse=False)
    assert [item['date'] for item in result] == [
        '2024-01-01T10:00:00',
        '2024-01-02T11:00:00',
        '2024-01-03T12:00:00',
        '2024-01-03T12:00:00',
    ]


# Проверка корректности при одинаковых датах
def test_sort_by_date_same_dates(sample_dates):
    result = sort_by_date(sample_dates, reverse=True)
    assert result[0]['id'] == 1
    assert result[1]['id'] == 4


# Проверка работы с некорректными данными
def test_sort_by_date_invalid_formats():
    data = [
        {'id': 1, 'date': '01.01.2024'},
        {'id': 2, 'date': '2024-01-02'},
    ]
    result = sort_by_date(data)
    assert len(result) == 2
