from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

#tentukan window/tab utama pada index ke-0
tab_utama = driver.window_handles[0]

#klik link yang membuka tab baru
driver.find_element(By.LINK_TEXT, "Click Here").click()
time.sleep(3)

#pindah ke tab utama
driver.switch_to.window(tab_utama)
time.sleep(3)

#klik link yang membuka tab baru
driver.find_element(By.LINK_TEXT, "Click Here").click()
time.sleep(3)

#pindah ke tab utama
driver.switch_to.window(tab_utama)
time.sleep(3)