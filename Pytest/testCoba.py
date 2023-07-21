from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
import pytest

driver = webdriver.Chrome()
driver.maximize_window()

parameter = [
    ("yahaha", "yohoho"),
    ("yasingammarkanari@gmail.com", "yohoho"),
    ("yahaha", "b0t0lm1num"),
    ("yasingammarkanari@gmail.com", "b0t0lm1num"),
]

@pytest.mark.parametrize("username, password", parameter)

def test_bukaWeb(username, password):
    for i in range(2):
        driver.get("https://tees.co.id/")
        driver.implicitly_wait(5)

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
            print("pop up tidak muncul")
            pass

    #malah coba negatif case login yahaha
    driver.find_element(By.XPATH, "//*[@id='navbar']/div[3]/submenu-navbar/div/div/ul[2]/li[3]").click()
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/login-view/div/div[2]/div/div/form/div[3]/button").click()
    validasi = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/login-view/div/div[2]/div/div/form/p").text
    print("Tidak dapat login syng")
    time.sleep(3)

    assert validasi == "Username atau password salah."

