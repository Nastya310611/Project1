from .masks import get_mask_card_number, get_mask_account
import datetime


def mask_account_card(mask: str) -> str:
    new_mask = mask.split()
    new_mask[1] = get_mask_card_number(new_mask[1])
    shifr_card = " ".join(new_mask)
    return shifr_card



shifr = mask_account_card('Visa 1234567890123456')
print(shifr)