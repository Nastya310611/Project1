from unittest.mock import MagicMock, patch

from src.external_api import convert_to_rub


def test_convert_to_rub_rub() -> None:
    """Конвертация рублей (API не должен вызываться)"""
    transaction = {"amount": 1000, "currency": "RUB"}
    result = convert_to_rub(transaction)
    assert result == 1000.0


# Успешная конвертация USD (мокаем requests.get)
@patch("src.external_api.requests.get")
def test_convert_to_rub_usd_success(mock_get) -> None:
    """Фейковый ответ от API"""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 9000.0}
    mock_get.return_value = mock_response

    transaction = {"amount": 100, "currency": "USD"}
    result = convert_to_rub(transaction)

    assert result == 9000.0
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_convert_to_rub_eur_success(mock_get) -> None:
    """Успешная конвертация EUR (мокаем requests.get)"""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 10000.0}
    mock_get.return_value = mock_response

    transaction = {"amount": 100, "currency": "EUR"}
    result = convert_to_rub(transaction)

    assert result == 10000.0


def test_convert_to_rub_unknown_currency() -> None:
    """Валюта неизвестна (например, GBP)"""
    transaction = {"amount": 100, "currency": "GBP"}
    result = convert_to_rub(transaction)
    assert result == 0.0
