import pytest

@pytest.fixture
def valid_card_number():
    return '1234567890123456'

@pytest.fixture
def invalid_card_number():
    return '123'


@pytest.fixture
def valid_account_number():
    return "1234567890123456"


@pytest.fixture
def invalid_account_number():
    return '32334'


