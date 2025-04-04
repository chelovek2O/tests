from selenium import webdriver

class BasePage:
    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser
        self.browser.implicitly_wait(5)

    def open(self, url):
        self.browser.get(url)

    def find_element(self, *args):
        return self.browser.find_element(*args)

    def implicitly_wait(self, time):
        self.browser.implicitly_wait(time)
