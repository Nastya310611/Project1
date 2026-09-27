from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account, mask_account_card

card_number = get_mask_card_number("1234567890123456")
print(card_number)

account_number = get_mask_account("1234567890123456")
print(account_number)

shifr_card = mask_account_card("Maestro 1596837868705199")
print(shifr_card)

shifr_account = mask_account("Счет 6468647367889477")
print(shifr_account)

data_string = get_date("2024-03-11T02:26:18.671407")
print(data_string)
