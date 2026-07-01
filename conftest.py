import pytest
from selenium import webdriver
import random

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    return driver

@pytest.fixture
def random_email():
    return f"user{random.randint(100, 999)}@test.yandex.ru"

@pytest.fixture
def ad_name():
    return f"Ad {random.randint(100, 999)}"

@pytest.fixture
def ad_description():
    return f"Description for ad {random.randint(100, 999)}"

@pytest.fixture
def ad_price():
    return random.randint(100, 5000)
