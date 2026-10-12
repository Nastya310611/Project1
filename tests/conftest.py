import pytest


@pytest.fixture
def valid_number_card():
    return '1234567890123456'


@pytest.fixture
def invalid_number_card():
    return '123'


@pytest.fixture
def invalid_number_card_2():
    return '23384847739291827737736647892'


@pytest.fixture
def valid_number_account():
    return '12345678901234567654'


@pytest.fixture
def invalid_number_account():
    return '123'


@pytest.fixture
def invalid_number_account_2():
    return '23384847739291827737736647892'


@pytest.fixture
def invalid_number_3():
    return '12356В7890123456'


@pytest.fixture
def invalid_number_4():
    return ''
