from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

driver = webdriver.Chrome()
driver.minimize_window()

parameter = [
    ("https://demoqa.com/", "DEMOQA"),
    ("https://jqueryui.com/", "jQuery UI")
]

@pytest.mark.parametrize("address, result", parameter)

def test_alamat(address, result):
    driver.get(address)
    title = driver.title

    assert title == result