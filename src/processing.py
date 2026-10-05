def filter_by_state(dict_state: list, state='EXECUTED') -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению"""
    new_dict_stage = []
    for d in dict_state:
        if d['state'] == state:
            new_dict_stage.append(d)
    return new_dict_stage


def sort_by_date(data: list, reverse: bool = True) -> list:
    """Функция сортирует список по дате"""
    return sorted(data, key=lambda item: item['date'], reverse=reverse)