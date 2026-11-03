import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE_PATH = os.path.join(BASE_DIR, "logs", "masks.log")
logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(LOG_FILE_PATH, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_num: str) -> str:
    """Функция для маскировки номера карты"""
    if card_num == "":
        logger.warning("Номер карты не был введен")
        return "Вы не ввели номер карты"
    if card_num.isdigit():
        if len(card_num) != 16:
            logger.error("Ввод некорректных данных")
            return "Введены некорректные данные, номер карты должен содержать 16 цифр"
        else:
            logger.info("Маскировка карты выполнена")
            return f"{card_num[0:4]} {card_num[4:6]}** **** {card_num[-4:]}"
    else:
        logger.error("Ввод некорректных данных")
        return "Номер карты должен содержать только цифры"


def get_mask_account(account_num: str) -> str:
    """Функция для маскировки номера счёта"""
    if account_num == "":
        logger.warning("Номер счета не был введен")
        return "Вы не ввели номер счета"
    if account_num.isdigit():
        if len(account_num) != 20:
            logger.error("Ввод некорректных данных")
            return "Введены некорректные данные, номер счета должен содержать 20 цифр"
        else:
            logger.info("Маскировка счета выполнена")
            return f"**{account_num[-4:]}"
    else:
        logger.error("Ввод некорректных данных")
        return "Номер счета должен содержать только цифры"
