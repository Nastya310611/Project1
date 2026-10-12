import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number_valid(valid_number_card):
    assert get_mask_card_number(valid_number_card) == '1234 56** **** 3456'


def test_get_mask_card_number_invalid(invalid_number_1):
    assert get_mask_card_number(invalid_number_1) == ('Введены некорректные данные, '
                                                      'номер карты должен содержать 16 цифр')


def test_get_mask_card_number_invalid_2(invalid_number_2):
    assert get_mask_card_number(invalid_number_2) == ('Введены некорректные данные, '
                                                      'номер карты должен содержать 16 цифр')


def test_get_mask_card_number_invalid_3(invalid_number_3):
    assert get_mask_card_number(invalid_number_3) == 'Номер карты должен содержать только цифры'


def test_get_mask_account_valid(valid_number_account):
    assert get_mask_account(valid_number_account) == '**7654'


def test_get_mask_account_invalid(invalid_number_1):
    assert get_mask_account(invalid_number_1) == 'Введены некорректные данные, номер счета должен содержать 20 цифр'


def test_get_mask_account_invalid_2(invalid_number_2):
    assert get_mask_account(invalid_number_2) == 'Введены некорректные данные, номер счета должен содержать 20 цифр'


def test_get_mask_account_invalid_3(invalid_number_3):
    assert get_mask_account(invalid_number_3) == 'Номер счета должен содержать только цифры'


def test_get_mask_account_invalid_4(invalid_number_4):
    assert get_mask_account(invalid_number_4) == 'Вы не ввели номер счета'


def test_get_mask_card_number_invalid_4(invalid_number_4):
    assert get_mask_card_number(invalid_number_4) == 'Вы не ввели номер карты'
