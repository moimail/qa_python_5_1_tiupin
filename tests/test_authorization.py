from data import Data
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import URLS
from locators import Locators as loc


class TestLoginMainPage:

    def test_auth_from_main_page(self,driver):
        # Вход через лавную страницу
        driver = driver
        driver.maximize_window()
        driver.get(URLS.MAIN_PAGE_URL)

        # Ожидание кнопки входа на главной странице
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((loc.LOGIN_TO_ACC_BUTTON)))
        # Нажатие на кнопку входа
        element = driver.find_element(*loc.LOGIN_TO_ACC_BUTTON)
        element.click()

        # Ожидание окна ввода данных
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((loc.LOGIN_FIELD)))
        #Ввод логина
        element = driver.find_element(*loc.LOGIN_FIELD)
        element.send_keys(Data.USER_NAME)
        #Ввод пароля
        element = driver.find_element(*loc.PASSFORD_FIELD)
        element.send_keys(Data.USER_PASSWORD)
        #Вход
        element = driver.find_element(*loc.LOGIN_BUTTON)
        element.click()
        #Проверка входа
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((loc.ORDER_BUTTON)))
        assert driver.find_element(*loc.ORDER_BUTTON)

    def test_auth_from_profile(self, driver):

        # Вход через личный кабинет
        driver = driver
        driver.maximize_window()
        driver.get(URLS.MAIN_PAGE_URL)

        #Переход по кнопке "Личный кабинет"
        # Ожидание кнопки "Личный кабинет" на главной странице
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((loc.PROFILE_BUTTON)))
        #Нажатие на кнопку "Личный кабинет"
        element = driver.find_element(*loc.PROFILE_BUTTON)
        element.click()
        # Ожидание окна ввода данных
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((loc.LOGIN_FIELD)))
        # Ввод логина
        element = driver.find_element(*loc.LOGIN_FIELD)
        element.send_keys(Data.USER_NAME)
        # Ввод пароля
        element = driver.find_element(*loc.PASSFORD_FIELD)
        element.send_keys(Data.USER_PASSWORD)
        # Вход
        element = driver.find_element(*loc.LOGIN_BUTTON)
        element.click()
        # Проверка входа
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((loc.ORDER_BUTTON)))
        assert driver.find_element(*loc.ORDER_BUTTON)

    def test_auth_from_registration_page(self,driver):

        # Вход через страницу регистрации
        driver = driver
        driver.maximize_window()
        driver.get(URLS.REG_PAGE_URL)

        # Переход по кнопке "Войти" со страницы регистрации
        # Ожидание гипперссылки "Войти" на странице регистрации
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((loc.GO_TO_LOGIN)))
        #Переход по гипперссылке "Войти"
        element = driver.find_element(*loc.GO_TO_LOGIN)
        element.click()
        # Ожидание окна ввода данных
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((loc.LOGIN_FIELD)))
        # Ввод логина
        element = driver.find_element(*loc.LOGIN_FIELD)
        element.send_keys(Data.USER_NAME)
        # Ввод пароля
        element = driver.find_element(*loc.PASSFORD_FIELD)
        element.send_keys(Data.USER_PASSWORD)
        # Вход
        element = driver.find_element(*loc.LOGIN_BUTTON)
        element.click()
        # Проверка входа
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((loc.ORDER_BUTTON)))
        assert driver.find_element(*loc.ORDER_BUTTON)

    def test_auth_from_recover_password_page(self, driver):

        # Вход через страницу восстановления пароля
        driver = driver
        driver.maximize_window()
        driver.get(URLS.RECOVER_PAGE_URL)

        # Переход по кнопке "Войти" со страницы восстановления пароля
        # Ожидание гипперссылки "Войти" на странице восстановления пароля
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((loc.GO_TO_LOGIN)))
        # Переход по гипперссылке "Войти"
        element = driver.find_element(*loc.GO_TO_LOGIN)
        element.click()
        # Ожидание окна ввода данных
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((loc.LOGIN_FIELD)))
        # Ввод логина
        element = driver.find_element(*loc.LOGIN_FIELD)
        element.send_keys(Data.USER_NAME)
        # Ввод пароля
        element = driver.find_element(*loc.PASSFORD_FIELD)
        element.send_keys(Data.USER_PASSWORD)
        # Вход
        element = driver.find_element(*loc.LOGIN_BUTTON)
        element.click()
        # Проверка входа
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((loc.ORDER_BUTTON)))
        assert driver.find_element(*loc.ORDER_BUTTON)









