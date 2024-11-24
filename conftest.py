import pytest
from selenium import webdriver

from data import BASE_PAGE_URL, ORDER_PAGE_URL


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(BASE_PAGE_URL)
    yield driver
    driver.quit()
