from .base_page import BasePage
from .locators import AuthLocators
from settings import Settings
import ast
import time
class AuthPage(BasePage):

    def __init__(self, driver, timeout=5, ):
        super().__init__(driver, timeout)
        url = Settings.base_url
        driver.get(url)

        self.number = driver.find_element(*AuthLocators.AUTH_NUMBER)
        self.email = driver.find_element(*AuthLocators.AUTH_EMAIL)
        self.login = driver.find_element(*AuthLocators.AUTH_LOGIN)
        self.ls = driver.find_element(*AuthLocators.AUTH_LS)
        self.password = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        self.authorization_form = driver.find_element(*AuthLocators.authorization_form)
        self.menu_tub = driver.find_element(*AuthLocators.menu_tub)
        self.tub_phone = driver.find_element(*AuthLocators.tub_phone)
        self.tub_mail = driver.find_element(*AuthLocators.tub_mail)
        self.tub_login = driver.find_element(*AuthLocators.tub_login)
        self.tub_personal_account = driver.find_element(*AuthLocators.tub_personal_account)
        self.page_left = driver.find_element(*AuthLocators.page_left)
        self.page_right = driver.find_element(*AuthLocators.page_right)
        self.active_tub_phone = driver.find_element(*AuthLocators.active_tub_phone)
        self.AUTH_ACTIVE_TAB = driver.find_element(*AuthLocators.AUTH_ACTIVE_TAB)
        self.forgot_password = driver.find_element(*AuthLocators.forgot_password)


    def find_other_element(self, by, location):
        return self.driver.find_element(by, location)

    def enter_email(self, value):
        self.email.send_keys(value)

    def enter_pass(self, value):
        self.password.send_keys(value)

    def btn_click(self):
        self.btn.click()
        time.sleep(1)


    def ls_click(self):
        self.tub_personal_account.click()

    def check_color(self, elem):
        rgba = elem.value_of_css_property('color')
        r, g, b, alpha = ast.literal_eval(rgba.strip('rgba'))
        hex_value = '#%02x%02x%02x' % (r, g, b)
        return hex_value
