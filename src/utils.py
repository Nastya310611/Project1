import json
import os

def load_operations(file_path: str) -> list:
    """Функция чтения JSON-файла"""
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data if isinstance(data, list) else []

    except json.JSONDecodeError:
        return []
