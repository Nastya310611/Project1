
def get_mask_card_number(card_num: str) -> str:
    """Функция для маскировки номера карты"""
    if len(card_num) < 16 or len(card_num) > 16:
        return "Введены некорректные данные, номер карты должен содержать 16 цифр"
    else:
        return f"{card_num[0:4]} {card_num[4:6]}** **** {card_num[-4:]}"


def get_mask_account(account_num: str) -> str:
    """Функция для маскировки номера счёта"""
    if len(account_num) < 16 or len(account_num) > 16:
        return "Введены некорректные данные, номер карты должен содержать 16 цифр"
    else:
        return f"**{account_num[-4:]}"
