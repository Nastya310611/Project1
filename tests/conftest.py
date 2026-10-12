import pytest


# Фикстура для функции get_mask_card_number в masks.py
@pytest.fixture
def valid_number_card():
    return '1234567890123456'


# Фикстура для функции get_mask_card_number в masks.py
@pytest.fixture
def invalid_number_1():
    return '123'


# Фикстура для функции get_mask_card_number
@pytest.fixture
def invalid_number_2():
    return '23384847739291827737736647892'


# Фикстура для функции get_mask_account
@pytest.fixture
def valid_number_account():
    return '12345678901234567654'


@pytest.fixture
def invalid_number_3():
    return '12356В7890123456'


@pytest.fixture
def invalid_number_4():
    return ''



