from selenium import webdriver

#panggil web driver
driver1 = webdriver.Chrome()
driver2 = webdriver.Chrome()
driver3 = webdriver.Chrome()

#membuka alamat web pada browser
driver1.get("https://www.google.com/")
driver2.get("https://www.gramedia.com/")
driver3.get("https://www.youtube.com/")
