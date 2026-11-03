import json
import os
import logging


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE_PATH = os.path.join(BASE_DIR, 'logs', 'utils.log')
logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(LOG_FILE_PATH, encoding='utf-8')
file_formatter = logging.Formatter('%(asktime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_operations(file_path: str) -> list:
    """Функция чтения JSON-файла"""
    if not os.path.exists(file_path):
        logger.warning(f'Файл {file_path} не найден')
        return []

    try:
        logger.info(f'Выполняем чтение файла')
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.info(f'Данные успешно прочитаны из файла {file_path}')
            return data if isinstance(data, list) else []

    except json.JSONDecodeError as ex:
        logger.error(f'Произошла ошибка чтения файла: {ex}')
        return []
