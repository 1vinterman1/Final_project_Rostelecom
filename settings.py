from random import choice
from string import ascii_lowercase

class Settings:
    chrome_driver = "C:\programs\Selenium_G\chromedriver_new.exe"
    base_url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope=openid&state=66cff6d6-62fd-409d-9c28-0f44b9d64d53&theme=light&auth_type'
    personal_account_url = 'https://b2c.passport.rt.ru/account_b2c/page?state=5f001c29-a73b-482a-980d-79a712922cde&client_id=account_b2c&theme=light#/'
    valid_number = '89188543178'
    valid_email = 'nikita_vinter@mail.ru'
    valid_login = 'lk_61064131'
    valid_ls = '461008749391'
    valid_password = '34495269Ros'
    russian_chars = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    chinese_chars = '的一是不了人我在有他这为之大来以个中上们'
    special_chars = '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'
    symbols_255 = "".join(choice(ascii_lowercase) for i in range(255))
    symbols_1000 = "".join(choice(ascii_lowercase) for i in range(1000))
    digit = '1234'
    menu_of_type_auth = ['Телефон', 'Почта', 'Логин', 'Лицевой счёт']
    invalid_number = '89189876543'
    invalid_email = 't@mail.ru'
    invalid_login = 'lk_21014111'
    invalid_ls = '361808789398'
    invalid_password = '9874561Tt'
    email_symbols_13 = 'test1@mail.ru'
    valid_first_name = 'Иван'
    valid_last_name = 'Иванов'
    valid_email_reg = 'ivanov123@mail.ru'
    valid_password_reg = '1234567Ii'
    valid_password_reg_other = '7654321Ii'
    valid_number_reg = '89881234578'
    valid_line = '-'
    password_symbols_7 = '12345Rr'
    password_no_caps = '12345678r'
    password_cyrillic = '1234567Юю'
    invalid_number_input_field = '111111'
