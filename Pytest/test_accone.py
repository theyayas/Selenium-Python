from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
import pytest

#menghilangkan logging
mode = webdriver.ChromeOptions()
mode.add_experimental_option('excludeSwitches', ['enable-logging'])

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(options=mode)
    driver.maximize_window()
    driver.get("https://os-test.acc.co.id/accone/Homepage")
    driver.implicitly_wait(15)

    yield driver

    driver.quit()

#=================================================================================================================
#                                                WELCOME PAGE
#=================================================================================================================

@pytest.mark.welcome
def test_welcome(setup):
    webTitle = setup.title
    tes = setup.find_element(By.XPATH, '//*[@id="b1-LayoutWrapper"]/div[3]/div[1]/div/div[1]/span').text
    #print(webTitle)

    assert tes == "Download aplikasi ACC ONE"

#=================================================================================================================
#                                                LOGIN WRONG
#=================================================================================================================

login_wrong = [
    ("yayaya@gsa.com", "yayaya1"),
    ("yiyiyi@gsa.com", "yiyiyi2"),
    ("yuyuyu@gsa.com", "yuyuyu3"),
    ("yeyeye@gsa.com", "yeyeye4"),
    ("yoyoyo@gsa.com", "yoyoyo5"),
]

@pytest.mark.login
@pytest.mark.parametrize("username, password", login_wrong)
def test_login(setup, username, password):
    setup.find_element(By.XPATH, '//*[@id="b4-$b3"]/div/a').click()
    setup.find_element(By.ID, "b5-Username").send_keys(username)
    setup.find_element(By.ID, "b5-Password2").send_keys(password)
    setup.find_element(By.ID, "b5-Button").click()

    try:
        alert = WebDriverWait(setup, 5).until(EC.alert_is_present())
        print(alert)
        assert "Username atau Password Salah" in alert #, f"Expected alert message not found: '{alert.text}'"

    except TimeoutException:
        print("berhasil login")

#=================================================================================================================
#                                             VALIDASI USERNAME
#=================================================================================================================

login_validasi_username = [
    ("yayaya"), 
    ("yayaya@hg"),
    ("yayehs.com")
]

@pytest.mark.validasi_username
@pytest.mark.parametrize("username", login_validasi_username)
def test_validasi_username(setup, username):
    setup.find_element(By.XPATH, '//*[@id="b4-$b3"]/div/a').click()
    setup.find_element(By.ID, "b5-Username").send_keys(username)
    validasi = setup.find_element(By.XPATH, '//*[@id="b5-b1-Input"]/span/span').text

    assert validasi == "Format email yang dimasukkan belum sesuai, Contoh : biko.maryono@gmail.com"

#=================================================================================================================
#                                             VALIDASI PASSWORD
#=================================================================================================================

login_validasi_password = [
    (" "), 
    ("yahaha"),
    ("yahahaha"),
    ("123456"),
    ("1234567")
]

@pytest.mark.validasi_password
@pytest.mark.parametrize("password", login_validasi_password)
def test_validasi_password(setup, password):
    setup.find_element(By.XPATH, '//*[@id="b4-$b3"]/div/a').click()
    setup.find_element(By.ID, "b5-Password2").send_keys(password)
    validasi = setup.find_element(By.XPATH, '//*[@id="b5-InputKataSandi3"]/span/span').text

    assert (validasi == "Kata Sandi harus diisi") or (validasi == "Kata Sandi minimal 7 Karakter") or (validasi == "Format belum sesuai")