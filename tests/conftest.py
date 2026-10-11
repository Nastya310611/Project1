import pytest

@pytest.fixture
def valid_card_number():
    return '1234567890123456'

@pytest.fixture
def invalid_card_number():
    return '123'


@pytest.fixture
def invalid_card_number_2():
    return '23384847739291827737736647892'


@pytest.fixture
def invalid_card_number_3():
    return '12356В7890123456'


@pytest.fixture
def valid_account_number():
    return "1234567890123456"


@pytest.fixture
def invalid_account_number():
    return '32334'


@pytest.fixture
def invalid_account_number_2():
    return '3233485678348348489384744444'


@pytest.fixture
def invalid_account_number_3():
    return "1234567K89012345"
