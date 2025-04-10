import time
import selenium
from selenium.webdriver.common.by import By
def test_google_search(browser):
    browser.get("https://google.com")
    search = browser.find_element(By.NAME,"q")
    search.send_keys("selenium grid")
    search.submit()
    time.sleep(5)