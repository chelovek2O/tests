from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_cart(self, product_name):
        self.find_element(*ProductPageLocators.COFELINK).click()
        search_box = self.find_element(*ProductPageLocators.INPUTER)
        search_box.click()
        search_box.send_keys(product_name)
        self.find_element(*ProductPageLocators.CONFBTN).click()
        self.find_element(*ProductPageLocators.BUYBTN).click()

    def is_product_added_successfully(self):
        return self.find_element(*ProductPageLocators.CONFERMER)
