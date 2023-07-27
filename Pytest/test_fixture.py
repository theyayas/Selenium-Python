from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
import pytest

# Menghilangkan error logging yang sebabnya tidak jelas
mode = webdriver.ChromeOptions()
mode.add_experimental_option('excludeSwitches', ['enable-logging'])

# Fixture : sebuah cara untuk menghindari pengulangan dalam codingan, dalam hal ini istilahnya adalah Don't Repat Yourself (DRY)
@pytest.fixture()
def setup():
    driver = webdriver.Chrome(options=mode)
    driver.maximize_window()
    driver.get("https://tees.co.id/")
    driver.implicitly_wait(10)
    
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]")))
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]").click()
    except TimeoutException:
        pass

    # Secara mudahnya line ini melempar step/langkah/kodingan keluar dari function ini (def (setup)) untuk digunakan pada fungsi lain
    # Hal ini digunakan dengan tujuan mengindari pengulangan step/langkah/kodingan
    # Caranya adalah dengan melempar nama fungsi ini (setup) sebagai parameter pada function yang menggunakannya
    yield driver    

    # Setelah satu function selesai, maka kembali ke function ini (setup)
    driver.quit()
'''------------------------------------------------- BATAS MANDATORY -------------------------------------------------'''

# Settingan tupple sebagai data inputan
register = [
    ("nama lengkap", "us3rn4m3ngabdi", "emailmengabdi@gg.com", "password")
]

login_wrong = [
    ("nama lengkap", "password"),
    ("yihihi", "yihihi"),
    ("yuhuhu", "yuhuhu"),
    ("yehehe", "yehehe"),
    ("yihiho", "yihiho"),
]

# Login
@pytest.mark.logintest
@pytest.mark.parametrize("nama, password", login_wrong)         # pytest.mark.parametrize untuk mengambil nilai-nilai dari tupple sebagai inputan
                                                                # syntaxnya gini ya sayang ("nama_parameter1, nama_parameter2", nama_tupple)
def test_login(setup, nama, password):
    setup.find_element(By.LINK_TEXT, 'Login').click()           # bukannya driver, tp nama function dari fixture
    setup.find_element(By.ID, 'username').send_keys(nama)
    setup.find_element(By.ID, 'password').send_keys(password)
    setup.find_element(By.XPATH, '/html/body/div[3]/div/div/login-view/div/div[2]/div/div/form/div[3]/button').click()
    penjagaan = setup.find_element(By.XPATH, '/html/body/div[3]/div/div/login-view/div/div[2]/div/div/form/p').text

    assert penjagaan == "Username atau password salah."         # Validasi

# Register
@pytest.mark.registertest
@pytest.mark.parametrize('nama, username, email, password', register)
def test_register(setup, nama, username, email, password):
    setup.find_element(By.LINK_TEXT, "Daftar").click()
    time.sleep(3)
    setup.execute_script("window.scrollTo(0, 200)")
    setup.find_element(By.ID, 'fullname').send_keys(nama)
    setup.find_element(By.ID, 'username').send_keys(username)
    setup.find_element(By.ID, 'email').send_keys(email)
    setup.find_element(By.ID, 'password').send_keys(password)
    setup.find_element(By.XPATH, '/html/body/div[3]/div/div/register-view/div[2]/form/div[2]/div/div/button').click()
    
    try:
        WebDriverWait(setup, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-logged"]/div/p')))
    except TimeoutException:
        pass

    validation = setup.find_element(By.XPATH, '//*[@id="user-logged"]/div/p').text
    assert validation == username