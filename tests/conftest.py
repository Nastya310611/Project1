import pytest


# Фикстура для функции get_mask_card_number в masks.py
@pytest.fixture
def valid_number_card():
    return '1234567890123456'


# Фикстура для функции get_mask_card_number и get_mask_account в masks.py
@pytest.fixture
def invalid_number_1():
    return '123'


# Фикстура для функций get_mask_card_number и get_mask_account в masks.py
@pytest.fixture
def invalid_number_2():
    return '23384847739291827737736647892'


# Фикстура для функции get_mask_account
@pytest.fixture
def valid_number_account():
    return '12345678901234567654'


# Фикстура для функций get_mask_card_number и get_mask_account в masks.py
@pytest.fixture
def invalid_number_3():
    return '12356В7890123456'


# Фикстура для функций get_mask_card_number и get_mask_account в masks.py
@pytest.fixture
def invalid_number_4():
    return ''


# Фикстура с данными для тестирования функции filter_by_state в widget.py
@pytest.fixture
def sample_transaction():
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2024-01-01T10:00:00'},
        {'id': 2, 'state': 'CANCELED', 'date': '2024-01-02T11:00:00'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2024-01-03T12:00:00'},
        {'id': 4, 'state': 'PENDING', 'date': '2024-01-04T13:00:00'},
        {'id': 5, 'state': 'CANCELED', 'date': '2024-01-05T14:00:00'},
    ]


# Фикстура с данными для тестирования функции sort_by_date в processing.py
@pytest.fixture
def sample_dates():
    return [
        {'id': 1, 'date': '2024-01-03T12:00:00'},
        {'id': 2, 'date': '2024-01-01T10:00:00'},
        {'id': 3, 'date': '2024-01-02T11:00:00'},
        {'id': 4, 'date': '2024-01-03T12:00:00'},  # Одинаковая дата с id=1
    ]
