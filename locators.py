from selenium.webdriver.common.by import By


class Locators:

    LOG_INTO_ACCOUNT_BUTTON = \
        (By.XPATH, "//*[contains(@class, 'button_button_size_large')]") # кнопка "Войти в аккаунт" на главной странице
    LOGIN_LOCATOR = (By.XPATH, "//*[contains(text(), 'Вход')]") # тэг "Вход"
    REGISTRATION_BUTTON_ON_LOGIN_PAGE = \
        (By.XPATH, "//*[contains(@class, 'Auth_link') and text()='Зарегистрироваться']") # кнопка "Зарегистрироваться" на странице входа
    REGISTRATION_LOCATOR = (By.XPATH, "//*[contains(text(), 'Регистрация')]") # тэг "Регистрация"
    NAME_INPUT = \
        (By.XPATH, "//*[text()='Имя']/following-sibling::input[@name='name']") # поле ввода имени
    EMAIL_INPUT = \
        (By.XPATH, "//*[text()='Email']/following-sibling::input[@name='name']") # поле ввода емейла
    PASSWORD_INPUT = \
        (By.XPATH, "//*[text()='Пароль']/following-sibling::input[@name='Пароль']") # поле ввода пароля
    REGISTRATION_BUTTON_ON_REG_PAGE = \
        (By.XPATH, "//*[contains(@class, 'button_button') and text()='Зарегистрироваться']") # кнопка "Зарегистрироваться" на странице регистрации
    INCORRECT_PASSWORD_LOCATOR = (By.XPATH, "//*[text()='Некорректный пароль']") # тэг некорректного пароля
    LOG_ON_BUTTON = \
        (By.XPATH, "//*[contains(@class, 'button_button') and text()='Войти']") # кнопка "Войти" на странице авторизации
    PLACE_ORDER_BUTTON = \
        (By.XPATH, "//*[contains(@class, 'button_button') and text()='Оформить заказ']") # кнопка "Оформить заказ"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//*[text()='Личный Кабинет']") # кнопка "Личный Кабинет"
    LOGIN_TEXT_BUTTON = \
        (By.XPATH, "//*[contains(@class, 'Auth_link') and text()='Войти']") # кнопка "Войти" на странице регистрации
    RESET_PASSWORD_BUTTON = \
        (By.XPATH, "//*[contains(@class, 'Auth_link') and text()='Восстановить пароль']") # кнопка "Восстановить пароль"
    ACCOUNT_TEXT_LOCATOR = (By.XPATH, "//main/div/nav/p[contains(@class, 'Account_text')]") # тэг текста в ЛК
    CONSTRUCTOR_BUTTON = (By.XPATH, "//*[contains(@class, 'AppHeader_header') and text()='Конструктор']")
    BUILD_A_BURGER_LOCATOR = (By.XPATH, "//*[text()='Соберите бургер']") # тэг "Соберите бургер"
    STELLAR_BURGER_LOGO = (By.XPATH, "//*[contains(@class, 'AppHeader_header__logo')]") # лого Stellar Burgers
    LOGOUT_BUTTON = (By.XPATH, "//*[text()='Выход']") # кнопка "Выход"
    BUNS_BUTTON = (By.XPATH, "//*[text()='Булки' and @class='text text_type_main-default']") # Кнопка "Булки"
    SAUCES_BUTTON = (By.XPATH, "//*[text()='Соусы' and @class='text text_type_main-default']") # Кнопка "Соусы"
    TOPPINGS_BUTTON = (By.XPATH, "//*[text()='Начинки' and @class='text text_type_main-default']") # Кнопка "Начинки"
    BUNS_LIST = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[1]") # Список булок
    SAUCES_LIST = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[2]") # Список соусов
    TOPPINGS_LIST = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[3]") # Список начинок
