import csv

import pandas as pd


def read_transactions_csv(file_path: str) -> list[dict]:
    """Считывает финансовые операции из CSV и возвращает список словарей"""
    with open(file_path, encoding="utf-8") as rd_file:
        reader = csv.DictReader(rd_file, delimiter=';')
        return [row for row in reader]


def read_transactions_excel(file_path: str) -> list[dict]:
    """Считывает финансовые операции из Excel и возвращает список словарей"""
    df = pd.read_excel("data/transactions_excel.xlsx")
    return df.to_dict(orient="records")
