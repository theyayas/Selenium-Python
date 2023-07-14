from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#panggil web driver
driver = webdriver.Chrome()
driver.maximize_window()

#membuka alamat web pada browser
driver.get("https://www.gramedia.com/login")

#mencari element 
#driver.find_element(By.ID, "mat-input-3").send_keys("yasingammarkanari@gmail.com")     #by id
driver.find_element(By.NAME, "email").send_keys("yasingammarkanari@gmail.com")
driver.find_element(By.NAME, "password").send_keys("H4l1dk4n4r1")                       #by name
#driver.find_element(By.LINK_TEXT, "MyValue").click()                                    #link text
#p = driver.find_elements(By.TAG_NAME, "p")                                              #by tag name
driver.find_element(By.CLASS_NAME, "submit").click()                                    #by class name
#driver.find_element(By.XPATH, '//*[@id="content"]/gm-login/div/div[1]/div/form/button') #by xpath - hati2 dengan tanda kutip ("")

#print(p)
time.sleep(10)

#driver.
