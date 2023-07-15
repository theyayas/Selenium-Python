from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/alerts")
time.sleep(3)

driver.find_element(By.ID, "alertButton").click()
time.sleep(3)

driver.switch_to.alert.accept()                     #accept
time.sleep(3)

driver.find_element(By.ID, "confirmButton").click()
time.sleep(3)

driver.switch_to.alert.dismiss()                    #dismiss
time.sleep(3)

driver.find_element(By.ID, "promtButton").click()   #mengisi prompt box
time.sleep(3)

driver.switch_to.alert.send_keys("i'm living in a dreamstate")
time.sleep(2)
driver.switch_to.alert.accept()                    #send keys, then ok
time.sleep(3)


