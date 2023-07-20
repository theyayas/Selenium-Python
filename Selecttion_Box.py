from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pyautogui
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get('https://demoqa.com/')
driver.execute_script('window.scrollTo(0,300)')
driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[4]/div/div[1]').click()
driver.execute_script('window.scrollTo(0,800)')
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[4]/div/ul/li[9]/span').click()

'''------------------------- OLD STYLE SELECTION -------------------------'''
driver.execute_script('window.scrollTo(0,500)')
pilihMenu = Select(driver.find_element(By.ID, 'oldSelectMenu'))
pilihMenu.select_by_visible_text('Aqua')
time.sleep(3)

'''------------------------- SELECT ONE -------------------------'''
driver.find_element(By.ID, 'selectOne').click()
pyautogui.typewrite('Mrs.')
pyautogui.press('enter')
time.sleep(3)