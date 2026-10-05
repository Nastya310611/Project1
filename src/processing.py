def filter_by_state(data_to_filter: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""
    filtered_state = []
    for d in data_to_filter:
        if d["state"] == state:
            filtered_state.append(d)
    return filtered_state


def sort_by_date(data: list, reverse: bool = True) -> list:
    """Функция сортирует список по дате"""
    return sorted(data, key=lambda item: item["date"], reverse=reverse)
