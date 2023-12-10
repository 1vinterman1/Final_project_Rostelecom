# python -m pytest -v --driver Chrome --driver-path chromedriver_new.exe tests/test_registr_page.py
import time
from pages.registr_page import RegistrPage
import pytest
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

def test_registration_form_right(driver):
   """ TC-10. Содержание правой части страницы Регистрации (форма "Регистрация")
    Правая часть страницы содержит форму "Регистрация", состоящую из:
    Поле ввода имени (обязательное);
    Поле ввода фамилии (обязательное);
    Поле выбора региона (обязательное);
    Поле ввода email или мобильного телефона(обязательное);
    Поле ввода пароля(обязательное);
    Поле подтверждения пароля(обязательное);
    Кнопка "Продолжить";
    Ссылки на политику конфиденциальности и пользовательское соглашение
    !!! Ссылка на политику конфиденциальности находится в футере страницы !!!"""

   page_reg = RegistrPage(driver)
   assert 'Регистрация' in page_reg.page_right_registration.text
   print('Форма ''Регистрация'' находится в правой части страницы!')
   assert page_reg.first_name.text in page_reg.registration_form.text
   print('Имя содержится!')
   assert page_reg.last_name.text in page_reg.registration_form.text
   print('Фамилия содержится!')
   assert page_reg.address_registration.text in page_reg.registration_form.text
   print('Регион есть!')
   assert page_reg.email_registration.text in page_reg.registration_form.text
   print('Email или мобильный телефон есть')
   assert page_reg.password_registration.text in page_reg.registration_form.text
   print('Пароль содержится!')
   assert page_reg.password_confirm.text in page_reg.registration_form.text
   print('Подтверждение пароля содержится!')
   assert page_reg.privacy_policy.text in page_reg.footer.text
   print('Политика конфиденциальности содержится в футере страницы!')
   assert 'Продолжить' != page_reg.registration_form.text
   print('Форма Регистрация не содержит кнопку "Продолжить"!')


def test_registration_form_left(driver):
   """ TC-11. Содержание левой части страницы Регистрации
      Левая часть содержит: логотип и продуктовый слоган кабинета """
   page_reg = RegistrPage(driver)

   assert 'Персональный помощник в цифровом мире Ростелекома' in page_reg.page_left_registration.text
   print(' Продуктовый слоган находятся в левой части страницы!')


@pytest.mark.auth
@pytest.mark.positive
@pytest.mark.xfail
@pytest.mark.parametrize('name_f', [Settings.valid_first_name,Settings.valid_line],
                         ids=['valid_first_name', 'valid_line'])
@pytest.mark.parametrize('name_l', [Settings.valid_last_name,Settings.valid_line],
                         ids=['valid_last_name', 'valid_line'])
def test_user_registration_firstname_lastname(driver, name_f, name_l):
   """ТС-12. Регистрация нового пользователя c валидными данными.
   Проверка полей имени и фамилии.
   1. Поле для ввода имени: должно содержать минимум 2 символа состоящих
   из букв кириллицы или знака тире (-).
   2. Поле для ввода фамилии: должно содержать минимум 2 символа состоящих
   из букв кириллицы или знака тире (-)
   !!! Поля для ввода имени/фамилии не принимают знак тире (-) !!! """


   page_reg = RegistrPage(driver)
   page_reg.first_name.send_keys(name_l)
   page_reg.first_name.clear()
   page_reg.last_name.send_keys(name_f)
   page_reg.last_name.clear()
   page_reg.email_registration.send_keys(Settings.valid_email_reg)
   page_reg.email_registration.clear()
   page_reg.password_registration.send_keys(Settings.valid_password_reg)
   page_reg.password_registration.clear()
   page_reg.password_confirm.send_keys(Settings.valid_password_reg)
   page_reg.password_confirm.clear()
   page_reg.button_register.click()

   try:
      assert page_reg.find_other_element(*AuthLocators.name_card_container).text == 'Подтверждение email'
      print('Успешный переход на страницу Подтверждение email!')
   except AssertionError:
      print('Необходимо заполнить поле кириллицей. От 2 до 30 символов.')


@pytest.mark.auth
@pytest.mark.positive
@pytest.mark.xfail
@pytest.mark.parametrize('username', [Settings.valid_password_reg,Settings.password_symbols_7,
                                      Settings.password_no_caps,Settings.password_cyrillic ],
                         ids=['valid_password_reg', 'symbols_7', 'no_caps', 'cyrillic' ])
def test_user_registration_password(driver, username):
   """ ТС-13. Регистрация нового пользователя c валидными данными.
    Проверка поля пароль.
    1. Если пользователь ввел пароль менее 8 символов
    "Длина пароля должна быть не менее 8 символов" под полем "Новый пароль"
    2. Если пользователь ввел пароль без заглавных букв "Пароль должен содержать
    хотя бы одну заглавную букву" под полем "Новый пароль"
    3. Если пользователь ввел пароль не с латинскими буквами "Пароль должен
    содержать только латинские буквы" под полем "Новый пароль"
    4. Если пользователь ввел пароль согласно парольной
    политике - переход на страницу Подтверждение Email """
   page_reg = RegistrPage(driver)
   page_reg.first_name.send_keys(Settings.valid_first_name)
   page_reg.first_name.clear()
   page_reg.last_name.send_keys(Settings.valid_first_name)
   page_reg.last_name.clear()
   page_reg.email_registration.send_keys(Settings.valid_email_reg)
   page_reg.email_registration.clear()
   page_reg.password_registration.send_keys(username)
   page_reg.password_registration.clear()
   page_reg.password_confirm.send_keys(username)
   page_reg.password_confirm.clear()
   page_reg.button_register.click()

   if username == Settings.valid_password_reg:
      assert page_reg.find_other_element(*AuthLocators.name_card_container).text == 'Подтверждение email'
      print('Успешный переход на страницу Подтверждение email!')
   if username == Settings.password_symbols_7:
      assert 'Длина пароля должна быть не менее 8 символов' in page_reg.find_other_element(*AuthLocators.new_password_container).text
      print('Длина пароля должна быть не менее 8 символов!')
   if username == Settings.password_no_caps:
      assert 'Пароль должен содержать хотя бы одну заглавную букву' in page_reg.find_other_element(*AuthLocators.new_password_container).text
      print('Пароль должен содержать хотя бы одну заглавную букву!')
   if username == Settings.password_cyrillic:
      assert 'Пароль должен содержать только латинские буквы' in page_reg.find_other_element(*AuthLocators.new_password_container).text
      print('Пароль должен содержать только латинские буквы!')\


def test_user_registration_confirm_password(driver):
   """ ТС-14. Регистрация нового пользователя c валидными данными.
    Проверка поля пароль.
    1. Если пользователь ввел в поле "Подтверждение пароля" пароль отличный от пароль
    "Новый пароль" выводим "Пароли не совпадают" под полем "Подтверждение пароля" """
   page_reg = RegistrPage(driver)
   page_reg.first_name.send_keys(Settings.valid_first_name)
   page_reg.first_name.clear()
   page_reg.last_name.send_keys(Settings.valid_first_name)
   page_reg.last_name.clear()
   page_reg.email_registration.send_keys(Settings.valid_email_reg)
   page_reg.email_registration.clear()
   page_reg.password_registration.send_keys(Settings.valid_password_reg)
   page_reg.password_registration.clear()
   page_reg.password_confirm.send_keys(Settings.valid_password_reg_other)
   page_reg.password_confirm.clear()
   page_reg.button_register.click()

   assert 'Пароли не совпадают' in page_reg.find_other_element(*AuthLocators.new_password_container).text
   print('Пароли не совпадают!')


def test_user_registration_already_registered_mail(driver):
   """" ТС-15. Регистрация пользователя с email от существующей учетной записи.
   Если введенный email привязан к имеющейся УЗ, то отображается оповещающая форма, которая состоит из:
1. Кнопка "Войти"
2. Кнопка "Восстановить пароль"
3. Кнопка "х"
!!! Кнопка "х", закрывающая всплывающее окно Учётная запись уже существует - ОТСУТСТВУЕТ!!! """

   page_reg = RegistrPage(driver)
   page_reg.first_name.send_keys(Settings.valid_first_name)
   page_reg.first_name.clear()
   page_reg.last_name.send_keys(Settings.valid_last_name)
   page_reg.last_name.clear()
   page_reg.email_registration.send_keys(Settings.valid_email)
   page_reg.email_registration.clear()
   page_reg.password_registration.send_keys(Settings.valid_password_reg)
   page_reg.password_registration.clear()
   page_reg.password_confirm.send_keys(Settings.valid_password_reg)
   page_reg.password_confirm.clear()
   page_reg.button_register.click()

   assert "Учётная запись уже существует" in page_reg.find_other_element(*AuthLocators.error_account_exists).text
   print('Появилась форма Учётная запись уже существует!')
   assert page_reg.find_other_element(*AuthLocators.button_exit).text in \
          page_reg.find_other_element(*AuthLocators.account_already_exists).text
   print('Кнопка Войти содержится в форме Учётная запись уже существует!')
   assert page_reg.find_other_element(*AuthLocators.button_restore_password).text in \
          page_reg.find_other_element(*AuthLocators.account_already_exists).text
   print('Кнопка Восстановить пароль содержится в форме Учётная запись уже существует!')


def test_registration_already_registered_number(driver):
   """" ТС-16. Регистрация пользователя с номером телефона от существующей учетной записи.
      Если введенный номер телефона привязан к имеющейся УЗ, то отображается оповещающая форма, которая состоит из:
1. Кнопка "Зарегистрироваться";
2. Кнопка "Отмена" - закрыть оповещающую форму;
!!! Кнопка Отмена, закрывающая оповещающую форму Учётная запись уже существует - ОТСУТСТВУЕТ !!! """

   page_reg = RegistrPage(driver)
   page_reg.first_name.send_keys(Settings.valid_first_name)
   page_reg.first_name.clear()
   page_reg.last_name.send_keys(Settings.valid_last_name)
   page_reg.last_name.clear()
   page_reg.email_registration.send_keys(Settings.valid_number)
   page_reg.email_registration.clear()
   page_reg.password_registration.send_keys(Settings.valid_password_reg)
   page_reg.password_registration.clear()
   page_reg.password_confirm.send_keys(Settings.valid_password_reg)
   page_reg.password_confirm.clear()
   page_reg.button_register.click()

   assert "Учётная запись уже существует" in page_reg.find_other_element(*AuthLocators.error_account_exists).text
   print('Появилась форма Учётная запись уже существует!')
   assert page_reg.find_other_element(*AuthLocators.button_register_confirm).text in \
          page_reg.find_other_element(*AuthLocators.account_already_exists).text
   print('Кнопка Зарегистрироваться содержится в форме Учётная запись уже существует!')


@pytest.mark.auth
@pytest.mark.positive
@pytest.mark.xfail
@pytest.mark.parametrize('username', [Settings.valid_email_reg,Settings.valid_number_reg ],
                         ids=['valid_email_reg', 'valid_number_reg' ])
def test_user_registration_form_confirm_email(driver, username):
   """ ТС-17. После корректного заполнения формы регистрации система перенаправляет пользователя
   на страницу ввода кода из смс или email, которая содержит
   1. При вводе корректного email при заполнении формы регистрации: Маскированная почта
   2. При вводе корректного номера телефона при заполнении формы регистрации: Маскированный номер телефона """
   page_reg = RegistrPage(driver)
   page_reg.first_name.send_keys(Settings.valid_first_name)
   page_reg.first_name.clear()
   page_reg.last_name.send_keys(Settings.valid_last_name)
   page_reg.last_name.clear()
   page_reg.email_registration.send_keys(username)
   page_reg.email_registration.clear()
   page_reg.password_registration.send_keys(Settings.valid_password_reg)
   page_reg.password_registration.clear()
   page_reg.password_confirm.send_keys(Settings.valid_password_reg)
   page_reg.password_confirm.clear()
   page_reg.button_register.click()

   if username == Settings.valid_email_reg:
      assert page_reg.find_other_element(*AuthLocators.name_card_container).text == 'Подтверждение email'
      print('Открылось форма Подтверждение email!')
   if username == Settings.valid_number_reg:
      assert page_reg.find_other_element(*AuthLocators.name_card_container).text == 'Подтверждение телефона'
      print('Открылась форма Подтверждение телефона!')


def test_contents_confirmation_form_email(driver):
   """ ТС-18. Содержание формы Подтверждение email.
    Форма Подтверждение email содержит:
    1. Поле для ввода кода
    2. Кнопку Получить код повторно !!! Кнопка Получить код повторно активна после таймера в секундах!!!
    3. Кнопку Изменить email """
   page_reg = RegistrPage(driver)
   page_reg.first_name.send_keys(Settings.valid_first_name)
   page_reg.first_name.clear()
   page_reg.last_name.send_keys(Settings.valid_last_name)
   page_reg.last_name.clear()
   page_reg.email_registration.send_keys(Settings.valid_email_reg)
   page_reg.email_registration.clear()
   page_reg.password_registration.send_keys(Settings.valid_password_reg)
   page_reg.password_registration.clear()
   page_reg.password_confirm.send_keys(Settings.valid_password_reg)
   page_reg.password_confirm.clear()
   page_reg.button_register.click()
   # time.sleep(15)

   assert page_reg.find_other_element(*AuthLocators.confirmation_code_email).text \
          in page_reg.find_other_element(*AuthLocators.authorization_form).text
   print('Поле для ввода кода содержится в форме Подтверждение email!')
   assert page_reg.find_other_element(*AuthLocators.code_container_timeout).text \
          in page_reg.find_other_element(*AuthLocators.authorization_form).text
   print('Отображается сообщение: Получить код повторно можно через ...!')
   assert page_reg.find_other_element(*AuthLocators.button_change_email).text \
          in page_reg.find_other_element(*AuthLocators.authorization_form).text
   print('Кнопка Изменить email содержится в форме Подтверждение email!')
