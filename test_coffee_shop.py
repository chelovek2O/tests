import pytest
from selenium import webdriver
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

def test_registration(browser):
    registration_page = RegistrationPage(browser)
    registration_page.open("https://coffeecuattro.ru/")
    registration_page.register("testo121", "testova121", "+7911200122", "testo125@gmail.com", "testo", "192322", "улица пушкина дом 23 к3 квартира 9")
    assert registration_page.is_registration_successful()

def test_login(browser):
    login_page = LoginPage(browser)
    login_page.open("https://coffeecuattro.ru/")
    login_page.login("testo125@gmail.com", "testo")
    assert login_page.is_login_successful()

def test_logout(browser):
    browser.delete_all_cookies()
    browser.get("https://coffeecuattro.ru/")
