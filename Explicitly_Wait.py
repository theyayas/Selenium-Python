from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/alerts")

driver.find_element(By.ID, "timerAlertButton").click()

try:
    WebDriverWait(driver, 3).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    time.sleep(2)
    print("Ketemu")
except TimeoutException:
    print("tidak ketemu")
    pass
