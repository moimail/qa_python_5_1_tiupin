from selenium.webdriver.common.by import By

class Locators:

    #Поля и кнопки для авторизации
    LOGIN_TO_ACC_BUTTON = ((By.XPATH, ".//button[text()='Войти в аккаунт']")) #Кнопка входа в аккуант
    LOGIN_FIELD = (By.XPATH, ('.//input[@name="name"]'))  #Поле ввода почты
    PASSFORD_FIELD = (By.XPATH, ('.//input[@name="Пароль"]'))  #Поле ввода пароля
    LOGIN_BUTTON = ((By.XPATH, ".//button[text()='Войти']"))  #Кнопка "Войти"
    GO_TO_LOGIN = (By.XPATH, "//a[text()='Войти']") #Гипперссылка на авторизацию через страницу регистрации

    #Личный кабинет
    ORDER_BUTTON = ((By.XPATH, ".//button[text()='Оформить заказ']")) #Кнопка "Оформить заказ"
    PROFILE_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']")  # Кнопка "Личный кабинет"
    LOGOUT = (By.XPATH, ".//button[text()='Выход']")

    #Конструктор
    BUNS_TAB = (By.XPATH, ".//span[text()='Булки']") #Вкладка "Булки"
    BUNS_AVAILABILITY = (By.XPATH, ".//p[text()='Краторная булка N-200i']") #Доступность булок
    SAUCE_TAB = (By.XPATH, ".//span[text() = 'Соусы']") #Вкладка "Соусы"
    SAUCE_AVAILABILITY = (By.XPATH, ".//p[text()='Соус Spicy-X']") #Доступность соусов
    FILLINGS_TAB = (By.XPATH, ".//span[text()='Начинки']")  #Вкладка "Начинки"
    FILLINGS_AVAILABILITY = (By.XPATH, ".//p[text()='Мясо бессмертных моллюсков Protostomia']") #Доступность начинок
    INGREDIENTS_LIST = (By.XPATH, ".//ul[starts-with(@class, 'BurgerIngredient')]") #Список ингредиентов
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']") #Кнопка "Конструктор"

    #Шапка
    LOGO = (By.XPATH, ".//header//div/a[@href='/']") #Логотип

    #Регистрация
    INCORRECT_PASSWORD = (By.XPATH, ".//p[text()='Некорректный пароль']") #Уведомление о не корректном пароле
    NAME_INPUT_FIELD = (By.XPATH, "//label[text()='Имя']/parent::div/input")  # Поле ввода имени пользователя
    EMAIL_INPUT_FIELD = (By.XPATH, ".//label[text() = 'Email']/parent::div/input")  # Поле ввода email
    PASSWORD_INPUT_FIELD = (By.XPATH, ".//label[text() = 'Пароль']/parent::div/input")  # поле ввода пароля
    REGISTRATION_BUTTON = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")  # Кнопка Зарегестрироваться