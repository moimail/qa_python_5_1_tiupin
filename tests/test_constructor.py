
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import URLS
from locators import Locators as loc

class TestConstructor:

    def test_go_to_sauce(self, driver):

        #Провекрка доступности соусов
        driver = driver
        driver.maximize_window()
        driver.get(URLS.MAIN_PAGE_URL)

        #Переход на вкулдку "Соусы"
        # Ожидание вклвдок конструктора
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((loc.INGREDIENTS_LIST)))
        #Переход во вкладку "Соусы"
        element = driver.find_element(*loc.SAUCE_TAB)
        element.click()
        #Проверка
        visible = WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((loc.SAUCE_AVAILABILITY)))
        assert visible

    def test_go_to_fillings(self, driver):

        # Провекрка доступности начинок
        driver = driver
        driver.maximize_window()
        driver.get(URLS.MAIN_PAGE_URL)

        # Переход на вкулдку "Начинки"
        # Ожидание вклвдок конструктора
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((loc.INGREDIENTS_LIST)))
        # Переход во вкладку "Начинки"
        element = driver.find_element(*loc.FILLINGS_TAB)
        element.click()
        # Проверка
        visible = WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((loc.FILLINGS_AVAILABILITY)))
        assert visible

    def test_go_to_buns(self, driver):

        # Провекрка доступности булок
        driver = driver
        driver.maximize_window()
        driver.get(URLS.MAIN_PAGE_URL)

        # Переход на вкладку "Начинки"
        # Ожидание вклвдок конструктора
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((loc.INGREDIENTS_LIST)))
        # Переход во вкладку "Начинки"
        element = driver.find_element(*loc.FILLINGS_TAB)
        element.click()
        #Переход во вкладку "Булки"
        element = driver.find_element(*loc.BUNS_TAB)
        element.click()
        # Проверка
        visible = WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((loc.BUNS_AVAILABILITY)))
        assert visible