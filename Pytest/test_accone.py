from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
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
    time.sleep(5)
    title = setup.title

    assert title == "Kredit Mobil & Fasilitas Dana - ACC"
    assert setup.find_element(By.XPATH, '//*[@id="$b5"]/div/div[3]/div/div/div/div[1]/div/a[1]/div/div[1]') is not None
    print("Beli Mobil Baru passed")
    print(title)
    assert setup.find_element(By.XPATH, '//*[@id="$b5"]/div/div[3]/div/div/div/div[1]/div/a[2]/div/div[1]/div[2]') is not None
    print("Beli Mobil Bekas passed")
    assert setup.find_element(By.XPATH, '//*[@id="$b5"]/div/div[3]/div/div/div/div[1]/div/a[3]/div/div[1]/div[2]') is not None
    print("Jual Mobil passed")
    assert setup.find_element(By.XPATH, '//*[@id="$b5"]/div/div[3]/div/div/div/div[2]/div[1]/div[1]').text == "Temukan Mobil Impianmu"
    print("Temukan Mobil Impianmu")
    assert setup.find_element(By.XPATH, '//*[@id="b5-b1-Column1"]/div[2]') is not None
    print("Kalkulator Kredit")

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
        alert = WebDriverWait(setup, 10).until(EC.alert_is_present())
        print(alert)
        assert "Username atau Password Salah" in alert #, f"Expected alert message not found: '{alert.text}'"

    except TimeoutException:
        raise Exception("salah") #print("berhasil login")

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
    time.sleep(3)

    assert (validasi == "Kata Sandi harus diisi") or (validasi == "Format belum sesuai") # or (validasi == "Kata Sandi minimal 7 Karakter") 
    print(validasi)

#=================================================================================================================
#                                                        YUNA
#=================================================================================================================

yuna_wrong = [
    ("sp736", "yahaha", "88"),
    ("spr4", "yahaha@muh", "88"),
    ("sp", "6732", "88r"),
]

@pytest.mark.yuna
@pytest.mark.parametrize("nama, email, nomor", yuna_wrong)
def test_validasi_yuna(setup, nama, email, nomor):
    setup.find_element(By.XPATH, '//*[@id="b1-b7-yuna_desktop"]').click()
    setup.find_element(By.XPATH, '//*[@id="b1-b7-$b2"]/div/div/div[3]/button[1]').click()
    time.sleep(2)

    setup.switch_to.frame(setup.find_element(By.TAG_NAME, 'iframe'))

    setup.find_element(By.XPATH, '//*[@id="name"]').send_keys(nama)
    setup.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
    setup.find_element(By.XPATH, '//*[@id="telephone"]').send_keys(nomor)
    setup.find_element(By.XPATH, '//*[@id="login"]/button').click()

    warning_name = setup.find_element(By.XPATH, '//*[@id="warning-name"]').text
    warning_email = setup.find_element(By.XPATH, '//*[@id="warning-email"]').text
    warning_number = setup.find_element(By.XPATH, '//*[@id="warning-phone"]').text

    assert warning_name is not None
    assert warning_name == "Invalid name min 3 chars alphabet"
    print(warning_name, " - Berhasil")

    assert warning_email is not None
    assert warning_email == "Please key in valid email address"
    print(warning_email, " - Berhasil")

    assert warning_number is not None
    assert warning_number == "Please enter minimum 10-12 digit"
    print(warning_number, " - Berhasil")


#=================================================================================================================
#                                                 BELI MOBIL
#=================================================================================================================

@pytest.mark.mobil_bekas
def test_mobil_bekas(setup):
    time.sleep(2)

    jual_beli = setup.find_element(By.LINK_TEXT, "Jual/Beli Mobil")
    jual_beli2 = ActionChains(setup).move_to_element(jual_beli)
    jual_beli2.perform()

    setup.find_element(By.LINK_TEXT, "Beli Mobil Bekas").click()
    time.sleep(2)

    title = setup.title

    assert title == "ACC | Daftar Harga Mobil Bekas"
    print("Berhasil masuk ke halaman", title)

    
#=================================================================================================================
#                                                FASILITAS DANA
#=================================================================================================================

@pytest.mark.fasilitas_dana
def test_fasilitas_dana(setup):
    setup.implicitly_wait(20)
    
    cari_dana = setup.find_element(By.LINK_TEXT, 'Cari Dana')
    cari_dana2 = ActionChains(setup).move_to_element(cari_dana)
    cari_dana2.perform()
    setup.find_element(By.LINK_TEXT, 'Fasilitas Dana').click()
    time.sleep(5)

    bpkb = setup.find_element(By.XPATH, '//*[@id="b5-b3-Column1"]/div/div[1]/img')
    bunga = setup.find_element(By.XPATH, '//*[@id="b5-b3-Column2"]/div/div[1]/img')
    pencairan_hingga = setup.find_element(By.XPATH, '//*[@id="b5-b3-Column3"]/div/div[1]/img')
    pencairan_cepat = setup.find_element(By.XPATH, '//*[@id="b5-b3-Column4"]/div/div[1]/img')
    cukup_isi_form = setup.find_element(By.XPATH, '//*[@id="b5-b3-Column5"]/div/div[1]/img')
    usia_mobil_hingga = setup.find_element(By.XPATH, '//*[@id="b5-b3-Column6"]/div/div[1]/img')

    assert bpkb is not None
    print("BPKB is present")

    assert bunga is not None
    print("Bunga is present")

    assert pencairan_hingga is not None
    print("Pencairan Hingga 85 persen Harga Mobil is present")

    assert pencairan_cepat is not None
    print("Pencairan Cepat is present")

    assert cukup_isi_form is not None
    print("Cukup Isi Form is present")

    assert usia_mobil_hingga is not None
    print("Usia Mobil Hingga 20 Tahun is present")

