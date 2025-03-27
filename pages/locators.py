from selenium.webdriver.common.by import By

class LoginPageLocators:
    MYACC = (By.ID, "modaltrigger") 
    PASSWORD = (By.ID, "password")  
    EMAIL = (By.ID, "email")  
    LGNBTN = (By.NAME,"loginbtn")
    CONFERMER = (By.CSS_SELECTOR,"#content > h1")

class ProductPageLocators:
    COFELINK = (By.LINK_TEXT, "КОФЕ")
    INPUTER = (By.CLASS_NAME, "form-control.input-lg")
    CONFBTN = (By.CSS_SELECTOR, "#search-column > span > button")
    BUYBTN =  (By.CSS_SELECTOR, "#content > div.product-grid.row > div:nth-child(1) > div > div.product-about > div.product-buttons > a")
    CONFERMER = (By.CLASS_NAME, "alert.alert-success")

class RegistrationPageLocators:
    TOPBTN = (By.CLASS_NAME, "top-panel-div-span")
    REGBTN = (By.LINK_TEXT, "Регистрация учетной записи")
    NAME = (By.ID, "register_firstname")
    SURNAME = (By.ID, "register_lastname")
    TEL = (By.ID, "register_telephone")
    EMAIL =(By.ID, "register_email")
    PASSWORD =(By.ID, "register_password")
    POSTCODE = (By.ID, "register_postcode")
    ADRES = (By.ID, "register_address_1")
    CONFERM = (By.ID, "simpleregister_button_confirm")
    NEXT = (By.LINK_TEXT, "ПРОДОЛЖИТЬ")
    CONFERMER = (By.CSS_SELECTOR, "#content > h1")