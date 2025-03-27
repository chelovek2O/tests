from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators
class LoginPage(BasePage):
    def login(self, email, password):
        self.find_element(*LoginPageLocators.MYACC).click()
        self.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        self.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        self.find_element(*LoginPageLocators.LGNBTN).click()

    def is_login_successful(self):
        return self.find_element(*LoginPageLocators.CONFERMER).text == "Личный кабинет"
