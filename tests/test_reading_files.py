from unittest.mock import mock_open, patch
import pandas as pd
from src.reading_files import read_transactions_csv, read_transactions_excel


# Тест для чтенис CSV
def test_read_transactions_csv_empty():
    """Тестируем корректное чтение файлов"""
    m = mock_open(read_data='')
    with patch('builtins.open', m):
        result = read_transactions_csv('fake_path.csv')
        assert result == []


# Тест для чтенис Excel
def test_read_transactions_excel_empty():
    """Тестируем корректное чтение файлов"""
    empty_df = pd.DataFrame()
    with patch('pandas.read_excel', return_value=empty_df):
        result = read_transactions_excel('fake_path.xlsx')
        assert result == []
