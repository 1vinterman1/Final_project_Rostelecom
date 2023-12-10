from .base_page import BasePage
from .locators import AuthLocators
import time

class RegistrPage(BasePage):

    def __init__(self, driver, timeout=2, ):
        super().__init__(driver, timeout)
        url = 'https://b2c.passport.rt.ru/'
        driver.get(url)
        driver.find_element(*AuthLocators.register_link).click()

        self.page_right_registration = driver.find_element(*AuthLocators.page_right_registration)
        self.page_left_registration = driver.find_element(*AuthLocators.page_left_registration)
        self.first_name = driver.find_element(*AuthLocators.first_name)
        self.last_name = driver.find_element(*AuthLocators.last_name)
        self.address_registration = driver.find_element(*AuthLocators.address_registration)
        self.email_registration = driver.find_element(*AuthLocators.email_registration)
        self.password_registration = driver.find_element(*AuthLocators.password_registration)
        self.password_confirm = driver.find_element(*AuthLocators.password_confirm)
        self.button_register = driver.find_element(*AuthLocators.button_register)
        self.registration_form = driver.find_element(*AuthLocators.registration_form)
        self.new_password_container = driver.find_element(*AuthLocators.new_password_container)
        self.authorization_form = driver.find_element(*AuthLocators.authorization_form)
        self.privacy_policy = driver.find_element(*AuthLocators.privacy_policy)
        self.footer = driver.find_element(*AuthLocators.footer)
    def find_other_element(self, by, location):
        return self.driver.find_element(by, location)

