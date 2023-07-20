from selenium import webdriver

# mengambil pilihan headless mode
mode = webdriver.ChromeOptions()
mode.headless = True

# menggunakan headless mode (bawah)
driver = webdriver.Chrome(options = mode)
driver.get('https://demoqa.com/select-menu')
print(driver.title)