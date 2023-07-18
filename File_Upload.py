from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
import pyautogui

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)

'''------------------------- CARA 1 -------------------------'''
driver.get('https://demoqa.com/')

driver.execute_script('window.scrollTo(0, 300)')    # cara scroll ke bawah
driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]').click()

driver.execute_script('window.scrollTo(0, 500)')    # cara scroll ke bawah
driver.find_element(By.ID, 'item-7').click()

'''
menggunakan send keys pada button "Upload". 
menggunakan path dari file dengan / (slash) -> bukan dengan \ (back slash)
hati-hati tidak semua website bisa menggunaka cara 1 ini
'''
driver.find_element(By.ID, 'uploadFile').send_keys('D:/Bismillahirrohmaanirrohim/Selenium-Python/Data_Dummy.pdf')
time.sleep(3)

'''------------------------- CARA 2 -------------------------'''
driver.get('https://gofile.io/welcome')
driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[3]/div/a/button').click()

driver.find_element(By.XPATH, '//*[@id="filesUpload"]/div/div[1]/div/button').click()
time.sleep(3)

# menggunakan pyautogui.write dan press
pyautogui.write(r'D:\Bismillahirrohmaanirrohim\Selenium-Python\Data_Dummy.pdf')
pyautogui.press('enter')
time.sleep(10)

try:
    WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mainUpload-03c93f4f-a426-4fdd-8a64-6bcfca061078"]/div/div/div[5]/div')))
    print('berhasil upload')
    driver.find_element(By.XPATH, '//*[@id="mainUpload-03c93f4f-a426-4fdd-8a64-6bcfca061078"]/div/div/div[10]/div/button').click()
    print('button sudah diklik')
except TimeoutException:
    print('tidak berhasil')
    pass

time.sleep(5)
