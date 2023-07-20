from selenium import webdriver

driver = webdriver.Chrome()
driver.minimize_window()

def test_bukaWeb():
    driver.get("https://demoqa.com/")
    title = driver.title                # akan digunakan sebagai validasi apakah web yang terbuka sudah benar

    assert title == "DEMOQA"            # validasi web yang terbuka adalah web DEMOQA

def test_bukaWebTheInternet():
    driver.get("https://the-internet.herokuapp.com/")
    title = driver.title                # akan digunakan sebagai validasi apakah web yang terbuka sudah benar

    assert title == "The Internet"      # validasi web yang terbuka adalah web The Internet