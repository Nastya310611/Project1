from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
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

data_to_filter = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
]

filled_state = filter_by_state(data_to_filter, state="CANCELED")
print(filled_state)


data_to_sort = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
]

sort_data = sort_by_date(data_to_sort)
print(sort_data)
