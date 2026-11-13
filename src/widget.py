from datetime import datetime

from .masks import get_mask_account, get_mask_card_number


def mask_account_card(mask: str) -> str:
    """Маскирует номер карты"""
    mask_str = str(mask).strip()
    if not mask_str:
        return ""
    if "Счет" in mask_str:
        return "Вы ввели номер счёта, а не номер карты"
    else:
        new_mask = mask_str.split()
        new_mask[-1] = get_mask_card_number(new_mask[-1])
        if new_mask[-1].startswith("Введены") or new_mask[-1].startswith("Номер карты"):
            return new_mask[-1]
        shifr_card = " ".join(new_mask)
        return shifr_card


def mask_account(mask: str) -> str:
    """Маскирует номер счёта"""
    if "Счет" not in mask:
        return "Вы ввели номер карты, а не номер счета"
    else:
        new_mask = mask.split()
        new_mask[-1] = get_mask_account(new_mask[-1])
        if new_mask[-1].startswith("Введены") or new_mask[-1].startswith("Номер счета"):
            return new_mask[-1]
        shifr_account = " ".join(new_mask)
        return shifr_account


def get_date(date_string: str) -> str:
    """Преобразует строку с датой из формата ISO в формат ДД.ММ.ГГГГ"""
    if not date_string:
        return ''
    if date_string.endswith('Z'):
        date_string = date_string[:-1]
    try:
        date_obj = datetime.fromisoformat(date_string)
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return date_string
