from selenium import webdriver

# mengambil pilihan headless mode
mode = webdriver.ChromeOptions()
mode.headless = True
mode.add_argument('--window-size=1366,768')

# menggunakan headless mode (bawah)
driver = webdriver.Chrome(options = mode)
driver.get('https://demoqa.com/select-menu')
print(driver.title)
driver.get_screenshot_as_file('screenshot2.jpg')