from random import random, randint
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import URLS
from locators import Locators as loc

class TestRegistrationPage:

    def test_registration_successful(self, driver):
        email = f'tiupin_{randint(100, 999)}@mail.ru'
        driver = driver
        driver.get(URLS.REG_PAGE_URL)

        #Ожидание открытия окна регистрации
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((loc.REGISTRATION_BUTTON)))
        #Ввод имени
        element = driver.find_element(*loc.NAME_INPUT_FIELD)
        element.send_keys('Иван')
        #Ввод почты
        element = driver.find_element(*loc.EMAIL_INPUT_FIELD)
        element.send_keys(email)
        #Ввод пароля
        element = driver.find_element(*loc.PASSWORD_INPUT_FIELD)
        element.send_keys("123456")
        #Регистрация
        element = driver.find_element(*loc.REGISTRATION_BUTTON)
        element.click()
        #Ожидание окна входа
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(loc.LOGIN_BUTTON))
        assert driver.current_url == URLS.AUTH_PAGE_URL

    def test_registration_short_password(self, driver):
        email = f'tiupin_{randint(100, 999)}@mail.ru'
        driver = driver
        driver.get(URLS.REG_PAGE_URL)

        # Ожидание открытия окна регистрации
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((loc.REGISTRATION_BUTTON)))
        # Ввод имени
        element = driver.find_element(*loc.NAME_INPUT_FIELD)
        element.send_keys('Иван')
        # Ввод почты
        element = driver.find_element(*loc.EMAIL_INPUT_FIELD)
        element.send_keys(email)
        # Ввод пароля
        element = driver.find_element(*loc.PASSWORD_INPUT_FIELD)
        element.send_keys("12345")
        # Регистрация
        element = driver.find_element(*loc.REGISTRATION_BUTTON)
        element.click()
        #Сообщение о не корректном пароле
        assert driver.find_element(*loc.INCORRECT_PASSWORD)
