from datetime import datetime

from .masks import get_mask_account, get_mask_card_number


def mask_account_card(mask: str) -> str:
    """Маскирует номер карты"""
    new_mask = mask.split()
    new_mask[1] = get_mask_card_number(new_mask[1])
    shifr_card = " ".join(new_mask)
    return shifr_card


def mask_account(mask: str) -> str:
    """Маскирует номер счёта"""
    new_mask = mask.split()
    new_mask[1] = get_mask_account(new_mask[1])
    shifr_card = " ".join(new_mask)
    return shifr_card


def get_date(date_string: str) -> str:
    """Преобразует строку с датой из формата ISO в формат ДД.ММ.ГГГГ"""
    date_obj = datetime.fromisoformat(date_string)
    return date_obj.strftime("%d.%m.%Y")
