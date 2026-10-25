from fileinput import filename

import pytest

from src.decorators import log


def test_log_success_console(capsys):
    """Проверка успешного выполнения(вывод в консоль)"""
    @log()
    def add(a, b):
        return a + b

    add(2, 3)
    captured = capsys.readouterr()
    assert 'add ok' in captured.out
    assert 'Result: 5' in captured.out
    assert 'Inputs: (2, 3), {}' not in captured.out


def test_log_success_file(cleanup_file):
    """Проверка успешного выполнения(запись в файл)"""
    filename = cleanup_file
    @log(filename=filename)
    def multiply(a, b):
        return a * b
    multiply(3, 4)
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    assert 'multiply ok'
    assert 'Result: 12' in content


def test_log_error_console(capsys):
    """Обработка исключений (вывод в консоль)"""
    @log()
    def divide(a, b):
        return a / b
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
    captured = capsys.readouterr()
    assert 'divide error:' in captured.out
    assert 'Inputs: (10, 0), {}' in captured.out
    assert 'division by zero' in captured.out


def test_log_error_file(cleanup_file):
    filename = cleanup_file
    @log(filename=filename)
    def get_item(lst, index):
        return lst[index]
    with pytest.raises(IndexError):
        get_item([1, 2], 5)
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    assert 'get_item error:' in content
    assert 'Inputs: ([1, 2], 5), {}' in content
    assert 'list index out of range' in content