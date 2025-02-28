import pytest
import requests
from unittest.mock import patch
from main import get_cat_image

@patch("requests.get")
def test_get_cat_image_success(mock_get):
    # Создаём фейковый ответ API
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{"url": "https://example.com/cat.jpg"}]

    # Проверяем, что функция возвращает этот URL
    result = get_cat_image()
    assert result == "https://example.com/cat.jpg"

@patch("requests.get")  # Мокируем запрос
def test_get_cat_image_failure(mock_get):
    # Делаем вид, что сервер вернул 404
    mock_get.return_value.status_code = 404

    # Проверяем, что функция вернёт None
    result = get_cat_image()
    assert result is None
