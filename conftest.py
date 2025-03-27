import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser_name",action="store",default="chrome",help="Выберите браузер: chrome или firefox")

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\n start Chrome")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\n start Firefox")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name должен быть chrome или firefox")
        
  
    
    yield browser
    
    print("\n quit browser")
    browser.quit()