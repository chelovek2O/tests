from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import RegistrationPageLocators
class RegistrationPage(BasePage):
    def register(self, firstname, lastname, telephone, email, password, postcode, address):
        self.find_element(*RegistrationPageLocators.TOPBTN).click()
        self.find_element(*RegistrationPageLocators.REGBTN).click()
        self.find_element(*RegistrationPageLocators.NAME).send_keys(firstname)
        self.find_element(*RegistrationPageLocators.SURNAME).send_keys(lastname)
        self.find_element(*RegistrationPageLocators.TEL).send_keys(telephone)
        self.find_element(*RegistrationPageLocators.EMAIL).send_keys(email)
        self.find_element(*RegistrationPageLocators.PASSWORD).send_keys(password)
        self.find_element(*RegistrationPageLocators.POSTCODE).send_keys(postcode)
        self.find_element(*RegistrationPageLocators.ADRES).send_keys(address)
        self.find_element(*RegistrationPageLocators.CONFERM).click()
        self.find_element(*RegistrationPageLocators.NEXT).click()

    def is_registration_successful(self):
        return self.find_element(*RegistrationPageLocators.CONFERMER).text == "Личный кабинет"
