from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://the-internet.herokuapp.com/')

driver.execute_script('window.scrollTo(0,500)')
driver.find_element(By.LINK_TEXT, 'Frames').click()

driver.find_element(By.LINK_TEXT, 'Nested Frames').click()

# mau masuk ke frame left
driver.switch_to.frame('frame-top')                     # karena frame left berada dalam frame top, maka masuk ke frame top dulu
driver.switch_to.frame('frame-left')                    # kemudian masuk ke dalam frame left
print(driver.find_element(By.XPATH, '/html/body').text)

# mau masuk ke frame middle, posisi sedang berada pada frame left
driver.switch_to.parent_frame()                         # karena frame middle berada dalam frame yang sama, maka pindah ke parent frame (top) dulu 
driver.switch_to.frame('frame-middle')                  # kemudian masuk ke dalam frame middle
print(driver.find_element(By.ID, 'content').text)

# mau masuk ke frame bottom, posisi deang berada pada frame middle
driver.switch_to.parent_frame()                         # naik satu kali ke frame top
driver.switch_to.parent_frame()                         # naik lagi ke frame utama
driver.switch_to.frame('frame-bottom')                  # kemudian masuk ke frame bottom
print(driver.find_element(By.XPATH, '/html/body').text)
#time.sleep(5)


