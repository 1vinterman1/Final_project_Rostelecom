33.1. Итоговый проект по автоматизации тестирования (PJ-04)

Автоматизированное тестирование страницы https://b2c.passport.rt.ru/ сайта "Ростелеком" с использованием PageObject, Selenium и PyTest.

Выполнение проекта:

1. Тестирование требований. Требования с комментариями находятся на google-диске. Ссылка на документ: https://drive.google.com/drive/folders/1sgLoP3pFQ4bYjj7bFME2M0evZipb3MOs?usp=drive_link

2. Разработаны чек-листы по авторизации и регистрации на сайте "Ростелеком".
Авторизация. Ссылка на google-диск: https://docs.google.com/spreadsheets/d/1J1A75sq1R10DfyJWJMBeZwIeo5flj93F/edit?usp=drive_link&ouid=109564838315212159739&rtpof=true&sd=true
Регистрация. Ссылка на google-диск: https://docs.google.com/spreadsheets/d/1prARsQX2BKmwKdGUgs4bHW4fed3GJT93/edit?usp=drive_link&ouid=109564838315212159739&rtpof=true&sd=true

3. Разработаны автоматизированные тесты в PyCharm, выложены на GitHub.

4. Оформлены баг-репорты с описанием багов, найденных в процессе тестирования.
   
Проект выполнен с использованием: PageObject, Selenium и PyTest.


Непосредственно в GitHub:

В корневой папке находятся файлы settings.py с тестовыми данными, chromedriver_new.exe -драйвер для бразера Chrome, requirements.txt для установки необходимых для тестирования библиотек.

Папка tests содержит файлы для запуска автотестов: test_auth_page.py - тесты для страницы авторизации, test_registr_page.py - тесты для страницы регистрации.

Папка pages содержит: locators.py - список локаторов на веб страницах, base_page.py - базовая страница, от которой унаследованы все остальные классы, 
auth_page.py - содержит класс для страницы авторизации, registr_page.py - содержит класс для страницы регистрации.

Запуск тестов осуществляется через команды:
Тесты авторизации: python -m pytest -v --driver Chrome --driver-path chromedriver_new.exe tests/test_auth_page.py
Тесты регистрации: python -m pytest -v --driver Chrome --driver-path chromedriver_new.exe tests/test_registr_page.py
