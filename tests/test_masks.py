import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number_valid(valid_card_number):
    assert get_mask_card_number(valid_card_number) == '1234 56** **** 3456'


def test_get_mask_card_number_invalid(invalid_card_number):
    assert get_mask_card_number(invalid_card_number) == "Введены некорректные данные, номер карты должен содержать 16 цифр"


def test_get_mask_card_number_invalid_2(invalid_card_number_2):
    assert get_mask_card_number(invalid_card_number_2) == "Введены некорректные данные, номер карты должен содержать 16 цифр"


def test_get_mask_account_valid(valid_account_number):
    assert get_mask_account(valid_account_number) == '**3456'


def test_get_mask_account_invalid(invalid_account_number):
    assert get_mask_account(invalid_account_number) == "Введены некорректные данные, номер счёта должен содержать 16 цифр"


def test_get_mask_account_invalid_2(invalid_account_number_2):
    assert get_mask_account(invalid_account_number_2) == "Введены некорректные данные, номер счёта должен содержать 16 цифр"