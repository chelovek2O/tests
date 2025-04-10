import pytest 
from selenium.webdriver.chrome.options import Options as chromeOptions
import selenium
from selenium import webdriver

@pytest.fixture
def browser():
    hub_url = "http://10.11.21.81:4444/wd/hub"
    options = chromeOptions()
    browser = webdriver.Remote(
        command_executor = hub_url,
        options = options
    )
    yield browser
    browser.quit()

