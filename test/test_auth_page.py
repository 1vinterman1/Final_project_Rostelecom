# python -m pytest -v --driver Chrome --driver-path chromedriver_new.exe tests/test_auth_page.py
import time
import pytest
from pages.auth_page import AuthPage
from settings import *
from selenium import webdriver
from pages.locators import AuthLocators
@pytest.fixture(autouse=True)
def driver():
   driver = webdriver.Chrome()
   # Переходим на страницу авторизации
   driver.get(Settings.base_url)

   driver.maximize_window()
   yield driver

   driver.quit()

def test_left_and_right_page(selenium):
   """ ТС-01. Проверка левой и правой частей страницы ( В левой части: меню аутентификаии,
   в правой части: продуктовый слоган ЛК "Ростелеком ID" и вспомогательная информация для клиента """
   try:
      page = AuthPage(selenium)
      assert 'Авторизация' in page.page_left.text
   except AssertionError:
      print('элемент АВТОРИЗАЦИЯ отсутствует в левой части страницы!')

   try:
      page = AuthPage(selenium)
      assert 'Персональный помощник в цифровом мире Ростелекома' in page.page_right.text
   except AssertionError:
      print('элемент ПРОДУКТОВЫЙ СЛОГАН отсутствует в правой части страницы!')


def test_authorization_form_location(driver):
   """ TC-02. В форме «Авторизация» расположено "Меню выбора типа аутентификации", содержащее:
   Таб "Номер", Таб "Почта", Таб "Логин", Таб "Лицевой счет"
   !!! Меню выбора типа аутентификации содержит таб "Телефон", а не "Номер" !!!"""
   page = AuthPage(driver)
   assert page.menu_tub.text in page.authorization_form.text
   assert page.tub_phone.text in page.authorization_form.text
   assert page.tub_mail.text in page.authorization_form.text
   assert page.tub_login.text in page.authorization_form.text
   assert page.tub_personal_account.text in page.authorization_form.text


def test_default_authentication_form(driver):
    """ ТС-03. По умолчанию выбрана форма авторизации по телефону """
    page = AuthPage(driver)
    assert page.active_tub_phone.text == Settings.menu_of_type_auth[0]


@pytest.mark.auth
@pytest.mark.positive
@pytest.mark.xfail
@pytest.mark.parametrize('name', [Settings.valid_number,Settings.invalid_number],
                         ids=['number', 'invalid_number'])

def test_authorization_phone_number(driver, name):
   """ TC-04. Авторизация по номеру телефона:
    1. При вводе валидного номера телефона + валидного пароля осуществляется переход в личный кабинет
    2. При вводе неправильного номера телефона или пароля выводится сообщение: 
    "Неверный логин или пароль" и элемент "Забыл пароль" перекрашивается в оранжевый цвет """
   page = AuthPage(driver)
   page.enter_email(name)
   page.enter_pass(Settings.valid_password)
   page.btn_click()

   if name == Settings.valid_number:
      assert page.get_relative_link() == '/account_b2c/page'
      print('Авторизация по номеру телефона прошла успешно!')
   elif name == Settings.invalid_number:
      error_mess = driver.find_element(*AuthLocators.AUTH_FORM_ERROR)
      forgot_pass = driver.find_element(*AuthLocators.AUTH_FORGOT_PASSWORD)
      assert error_mess.text == 'Неверный логин или пароль' and \
             page.check_color(forgot_pass) == '#ff4f12'
      print('Неверный логин или пароль!')


@pytest.mark.auth
@pytest.mark.positive
@pytest.mark.xfail
@pytest.mark.parametrize('username', [Settings.valid_email,Settings.invalid_email, Settings.email_symbols_13 ],
                         ids=['email', 'invalid_email', '12_symbols'])

def test_authorization_email(driver, username):
   """ ТС-05. Авторизация через почту:
    1. При вводе валидной почты + валидного пароля осуществляется переход в личный кабинет
    2. При вводе неправильной почты или пароля выводится сообщение:
    "Неверный логин или пароль" и элемент "Забыл пароль" перекрашивается в оранжевый цвет
    3. Ограничение на ввод 12 цифр и подсказка под символами в виде нижних подчеркиваний
    !!! Ограничение на ввод 12 цифр и подсказка под символами в виде нижних подчеркиваний - НЕ СРАБАТЫВАЕТ !!!"""
   page = AuthPage(driver)
   page.enter_email(username)
   page.enter_pass(Settings.valid_password)
   page.btn_click()

   if username == Settings.valid_email:
      assert page.get_relative_link() == '/account_b2c/page'
      print('Авторизация по почте прошла успешно!')
   elif username == Settings.invalid_email:
      error_mess = driver.find_element(*AuthLocators.AUTH_FORM_ERROR)
      forgot_pass = driver.find_element(*AuthLocators.AUTH_FORGOT_PASSWORD)
      assert error_mess.text == 'Неверный логин или пароль' and \
             page.check_color(forgot_pass) == '#ff4f12'
      print('Неверный логин или пароль!')
   elif username == Settings.email_symbols_13:
      error_mess = driver.find_element(*AuthLocators.AUTH_FORM_ERROR)
      forgot_pass = driver.find_element(*AuthLocators.AUTH_FORGOT_PASSWORD)
      assert error_mess.text == 'Неверный логин или пароль' and \
             page.check_color(forgot_pass) == '#ff4f12'
      print('Ограничение на ввод не больше 12 символов не сработало!')


@pytest.mark.auth
@pytest.mark.positive
@pytest.mark.xfail
@pytest.mark.parametrize('username', [Settings.valid_login,Settings.invalid_login ],
                         ids=['login', 'invalid_login'])
def test_authorization_login(driver, username):
   """ TC-06. Авторизация по логину:
      1. При вводе валидного логина + валидного пароля осуществляется переход в личный кабинет
      2. При вводе неправильного логина или пароля выводится сообщение:
      "Неверный логин или пароль" и элемент "Забыл пароль" перекрашивается в оранжевый цвет """
   page = AuthPage(driver)
   page.enter_email(username)
   page.enter_pass(Settings.valid_password)
   page.btn_click()

   if username == Settings.valid_login:
      assert page.get_relative_link() == '/account_b2c/page'
      print('Авторизация по логину прошла успешно!')
   elif username == Settings.invalid_login:
      error_mess = driver.find_element(*AuthLocators.AUTH_FORM_ERROR)
      forgot_pass = driver.find_element(*AuthLocators.AUTH_FORGOT_PASSWORD)
      assert error_mess.text == 'Неверный логин или пароль' and \
             page.check_color(forgot_pass) == '#ff4f12'
      print('Неверный логин или пароль!')


def test_authorization_valid_ls(driver):
   """ ТС-07.Авторизация по валидному лицевому счету.
   При вводе валидного лицевого счета + валидного пароля осуществляется переход в личный кабинет
   !!!Чтобы авторизоваться по валидному лицевому счету, нужно самостоятельно переключиться
   на таб Лицевой счет!!! """
   page = AuthPage(driver)
   page.ls_click()
   page.enter_email(Settings.valid_ls)
   page.enter_pass(Settings.valid_password)
   page.btn_click()

   assert page.get_relative_link() == '/account_b2c/page'
   print('Авторизация по логину прошла успешно!')


@pytest.mark.auth
@pytest.mark.positive
@pytest.mark.xfail
@pytest.mark.parametrize('username', [Settings.valid_password,Settings.invalid_password ],
                         ids=['valid_password', 'invalid_password'])
def test_authorization_invalid_ls(driver, username):
   """ TC-08. Авторизация по некорректному лицевому счету:
      При вводе неправильного лицевого счета или пароля выводится сообщение:
      "Неверный логин или пароль" и элемент "Забыл пароль" перекрашивается в оранжевый цвет
      !!!НЕ ПРОИСХОДИТ АВТОМАТИЧЕСКОЕ ПЕРЕКЛЮЧЕНИЯ ТАБА НА ЛИЦЕВОЙ
      СЧЕТ ПРИ ВВОДЕ ЛИЦЕВОГО СЧЕТА В ПОЛЕ ПО УМОЛЧАНИЮ(ТЕЛЕФОН)!!!"""
   page = AuthPage(driver)
   page.enter_email(Settings.invalid_ls)
   page.enter_pass(username)
   time.sleep(15) # ждем 15 секунд, чтобы ввести буквы с Captcha, если она появится
   page.btn_click()

   error_mess = driver.find_element(*AuthLocators.AUTH_FORM_ERROR)
   forgot_pass = driver.find_element(*AuthLocators.AUTH_FORGOT_PASSWORD)
   if username == Settings.valid_password:
      assert error_mess.text == 'Неверный логин или пароль' and \
             page.check_color(forgot_pass) == '#ff4f12'
      print('Неверный логин или пароль!')
   if username == Settings.invalid_password:
      assert error_mess.text == 'Неверный логин или пароль' and \
             page.check_color(forgot_pass) == '#ff4f12'
      print('Неверный логин или пароль!')


def test_back_to_otp_content(driver):
   """ TC-09. Содержание формы "Авторизация по временному коду"
   Форма "Авторизация по коду" содержит:
   1) форму “Укажите контактный номер телефона
   или почту, на которые необходимо отправить код подтверждения
   2) Поле ввода номера телефона или почты
   3) Кнопку "Получить код
   !!! Форма авторизации не содержит форму "Войти по временному коду"!!! """
   page = AuthPage(driver)
   try:
      assert 'Войти по временному коду' in page.authorization_form.text
   except AssertionError:
      print('Форма авторизации не содержит форму "Войти по временному коду"')
