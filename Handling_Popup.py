from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tees.co.id/")
driver.implicitly_wait(2)

'''
menggunakan WebDriverWait, expected_condition, dan TimeoutException untuk menunggu apakah pup up muncul atau tidak
karena pop up seperti ini kadang muncul, kadang tidak muncul
'''
try:
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div")))
    print("popup muncul")
    driver.find_element(By.CLASS_NAME, "btn-modal-close").click()
    print("popup ditutup")
except  TimeoutException:
    print("tidak muncul")
    pass

#malah coba negatif case login yahaha
driver.find_element(By.XPATH, "//*[@id='navbar']/div[3]/submenu-navbar/div/div/ul[2]/li[3]").click()
driver.find_element(By.ID, "username").send_keys("yahahaha")
driver.find_element(By.ID, "password").send_keys("yohohoho")
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/login-view/div/div[2]/div/div/form/div[3]/button").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/login-view/div/div[2]/div/div/form/p").is_displayed()
print("Tidak dapat login syng")
time.sleep(3)

'''try:
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/login-view/div/div[2]/div/div/form/div[3]/button")))
    print("bisa diklik")
except TimeoutException:
    print("tidak dapat diklik")'''

