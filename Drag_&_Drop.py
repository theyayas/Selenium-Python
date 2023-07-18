from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get('https://demoqa.com/')

driver.execute_script('window.scrollTo(0,300)')
driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[5]/div/div[1]').click()
time.sleep(3)

driver.execute_script('window.scrollTo(0,500)')
driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[5]/div/ul'))
driver. find_element(By.XPATH, '//*[@id="item-3"]').click()

dragable = driver.find_element(By.ID, 'draggable')
dropable = driver.find_element(By.ID, 'droppable')
action = ActionChains(driver)

action.drag_and_drop(dragable, dropable).perform()
time.sleep(3)