from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get('https://demoqa.com/droppable')

dragable = driver.find_element(By.ID, 'draggable')
dropable = driver.find_element(By.ID, 'droppable')
action = ActionChains(driver)

action.drag_and_drop(dragable, dropable).perform()
time.sleep(3)