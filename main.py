from src.masks import get_mask_card_number, get_mask_account

card_number = get_mask_card_number("1234567890123456")
print(card_number)

account_number = get_mask_account("1234567890123456")
print(account_number)