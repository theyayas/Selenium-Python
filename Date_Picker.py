from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

'''------------------------- CARA 1 -------------------------'''
driver.get('https://jqueryui.com/')

driver.execute_script('window.scrollTo, (0,300)')
driver.find_element(By.LINK_TEXT, 'Datepicker').click()

driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="content"]/iframe'))
driver.find_element(By.XPATH, '//*[@id="datepicker"]').send_keys('07/13/2023')
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="datepicker"]').clear()
driver.find_element(By.XPATH, '//*[@id="datepicker"]').send_keys('01/08/2023')  
#driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[4]/td[6]/a').click()
time.sleep(5)

'''------------------------- CARA 2 -------------------------'''
driver.get('https://demoqa.com/date-picker')

driver.find_element(By.ID, 'datePickerMonthYearInput').click()

pyautogui.keyDown('ctrl')       # tahan tombol ctrl
pyautogui.press('a')            # tekan tombol a untuk select all
pyautogui.keyUp('ctrl')         # lepas tombol ctrl
pyautogui.press('backspace')    # hapus text yang sudah diselect

driver.find_element(By.ID, 'datePickerMonthYearInput').send_keys('01/01/2023')

time.sleep(5)

