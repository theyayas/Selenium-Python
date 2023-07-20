from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

def test_bukaWeb():
    driver.get("https://demoqa.com/")
    title = driver.title                # akan digunakan sebagai validasi apakah web yang terbuka sudah benar

    assert title == "DEMOQA"             # validasi web yang terbuka adalah web DEMOQA iya