# Sprint_5
# Проект UI-тестирования сайта объявлений

## Описание
Автотесты для проверки регистрации, авторизации, выхода из системы и создания объявлений.

## Технологии
- pytest
- Selenium WebDriver

## Структура проекта
- `tests/test_registration.py` — тесты регистрации пользователя
- `tests/test_authorization.py` — тесты логина и логаута
- `tests/test_ads_creation.py` — тесты создания объявлений
- `conftest.py` — фикстуры
- `locators.py` — локаторы элементов

## Запуск
- python -m pytest tests
