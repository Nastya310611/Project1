import pytest

from src.masks import get_mask_card_number


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "1234 56** **** 3456"