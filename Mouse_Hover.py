from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains    # PENTING

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://demoqa.com/menu')
driver.implicitly_wait(3)

menu = driver.find_element(By.LINK_TEXT, 'Main Item 2')
hover = ActionChains(driver).move_to_element(menu)                  # PENTING
hover.perform()
print('berhasil')

menu2 = driver.find_element(By.LINK_TEXT, 'SUB SUB LIST »')
hover2 = ActionChains(driver).move_to_element(menu2)                # PENTING
hover2.perform()
print('berhasil2')

driver.find_element(By.LINK_TEXT, 'Sub Sub Item 2').is_enabled()
print('berhasil semuanya yahaha')