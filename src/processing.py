import re


def filter_by_state(dict_state: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""
    new_dict_stage = []
    for item in dict_state:
        item_state = item.get('state')
        if item_state is not None and str(item_state).lower() == state.lower():
            new_dict_stage.append(item)
    return new_dict_stage


def process_bank_search(data:list[dict], search:str)->list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей, у которых в описании есть данная строка"""
    data_with_search = []
    pattern = re.compile(search, re.IGNORECASE)
    for operation in data:
        description = operation.get('description', '')
        if pattern.search(description):
            data_with_search.append(operation)
    return data_with_search


def sort_by_date(data: list, reverse: bool = True) -> list:
    """Функция сортирует список по дате"""
    return sorted(data, key=lambda item: item["date"], reverse=reverse)
