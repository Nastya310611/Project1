import json
from unittest.mock import mock_open, patch
from src.utils import load_operations  # Убедитесь, что путь импорта верный!


@patch('src.utils.os.path.exists')
def test_load_operations_file_not_found(mock_exists):
    """Файл не найден"""
    mock_exists.return_value = False
    result = load_operations('fake_path.json')
    assert result == []


@patch('src.utils.os.path.exists')
@patch('builtins.open', new_callable=mock_open, read_data="")
def test_load_operations_empty_file(mock_file, mock_exists):
    """Файл пустой"""
    mock_exists.return_value = True
    result = load_operations('fake_path.json')
    assert result == []


@patch('src.utils.os.path.exists')
@patch('builtins.open', new_callable=mock_open, read_data='{"key": "value"}')
def test_load_operations_not_a_list(mock_file, mock_exists):
    """В файле не список"""
    mock_exists.return_value = True
    result = load_operations('fake_path.json')
    assert result == []


@patch('src.utils.os.path.exists')
@patch('builtins.open', new_callable=mock_open, read_data='[{"id": 1, "amount": 100}]')
def test_load_operations_success(mock_file, mock_exists):
    """Успешное чтение"""
    mock_exists.return_value = True
    result = load_operations('fake_path.json')
    assert result == [{"id": 1, "amount": 100}]