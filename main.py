from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, mask_account

card_number = get_mask_card_number("1234567890123456")
print(card_number)

account_number = get_mask_account("1234567890123456")
print(account_number)

shifr_card = mask_account_card('Maestro 1596837868705199')
print(shifr_card)

shifr_account = mask_account('Счет 64686473678894779589')
print(shifr_account)
