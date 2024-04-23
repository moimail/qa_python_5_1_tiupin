from data import Data
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import URLS
from locators import Locators as loc

class TestProfilePage:

    def test_go_to_profile_button(self,driver):
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
        #Переход в личный кабинет
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((loc.PROFILE_BUTTON)))
        element = driver.find_element(*loc.PROFILE_BUTTON)
        element.click()
        #Ожидание открытия личного кабинета
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(loc.LOGIN_FIELD))
        assert driver.find_element(*loc.LOGIN_FIELD).get_attribute('value') == Data.USER_NAME

    def test_go_to_constructor_button(self, driver):

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
        # Ввод логина
        element = driver.find_element(*loc.LOGIN_FIELD)
        element.send_keys(Data.USER_NAME)
        # Ввод пароля
        element = driver.find_element(*loc.PASSFORD_FIELD)
        element.send_keys(Data.USER_PASSWORD)
        # Вход
        element = driver.find_element(*loc.LOGIN_BUTTON)
        element.click()
        #Ожидание кнопки "Конструктор"
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((loc.CONSTRUCTOR_BUTTON)))
        element = driver.find_element(*loc.CONSTRUCTOR_BUTTON)
        element.click()
        #Проверка кнопки "Конструктор"
        assert driver.current_url == URLS.MAIN_PAGE_URL

    def test_go_to_logo(self, driver):
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
        # Ввод логина
        element = driver.find_element(*loc.LOGIN_FIELD)
        element.send_keys(Data.USER_NAME)
        # Ввод пароля
        element = driver.find_element(*loc.PASSFORD_FIELD)
        element.send_keys(Data.USER_PASSWORD)
        # Вход
        element = driver.find_element(*loc.LOGIN_BUTTON)
        element.click()
        #Ожидание логотипа
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((loc.LOGO)))
        #Переход по логотипу
        element = driver.find_element(*loc.LOGO)
        element.click()
        # Проверка перехода по логитипу
        assert driver.current_url == URLS.MAIN_PAGE_URL


    def test_logout(self, driver):
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
        # Ввод логина
        element = driver.find_element(*loc.LOGIN_FIELD)
        element.send_keys(Data.USER_NAME)
        # Ввод пароля
        element = driver.find_element(*loc.PASSFORD_FIELD)
        element.send_keys(Data.USER_PASSWORD)
        # Вход
        element = driver.find_element(*loc.LOGIN_BUTTON)
        element.click()
        # Переход в личный кабинет
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((loc.PROFILE_BUTTON)))
        element = driver.find_element(*loc.PROFILE_BUTTON)
        element.click()
        #Выход из учетной записи
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((loc.LOGOUT)))
        element = driver.find_element(*loc.LOGOUT)
        element.click()
        #Проверка выхода
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((loc.LOGIN_BUTTON)))
        assert driver.current_url == URLS.AUTH_PAGE_URL
