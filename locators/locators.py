from selenium.webdriver.common.by import By


class TestLocators:
    SEARCH_BUTTON_LOGIN_ACCOUNT = By.XPATH, ".//button[text()='Войти в аккаунт']"  # Кнопка войти в аккаунт
    SEARCH_BUTTON_LOGIN = By.XPATH, ".//h2[text()='Вход']"  # Кнопка Вход
    SEARCH_INPUT_EMAIL = By.XPATH, ".//*[text()='Email']/following-sibling::input"  # Поле для ввода email
    SEARCH_INPUT_PASSWORD = By.XPATH, ".//*[text()='Пароль']/following-sibling::input"  # Поле для ввода пароля
    CLICK_BUTTON_LOGIN = By.XPATH, ".//button[text()='Войти']"  # Кнопка Войти
    SEARCH_BUTTON_ORDER = By.XPATH, ".//button[text()='Оформить заказ']"  # Кнопка Оформить заказ
    SEARCH_BUTTON_PERSONAL_ACCOUNT = By.XPATH, ".//*[text()='Личный Кабинет']"  # Кнопка Личный кабинет
    CHECK_BUTTON_LOGIN = By.XPATH, ".//a[text()='Войти']"  # Кнопка Войти

    SEARCH_TEXT_PROFILE = By.XPATH, ".//a[text()='Профиль']"  # Кнопка Профиль
    SEARCH_BUTTON_LOGOUT = By.XPATH, ".//button[text()='Выход']"  # Кнопка Выход

    SEARCH_BUTTON_CONSTRUCTOR = By.XPATH, ".//p[text()='Конструктор']"  # Кнопка Конструктор
    SEARCH_BUTTON_LOGO = By.XPATH, ".//*[contains(@class, 'AppHeader_header__logo')]"  # Картинка логотипа

    SEARCH_INPUT_NAME = By.XPATH, ".//*[text()='Имя']/following-sibling::input"  # Поле для ввода имени
    CHECK_BUTTON_REGISTRATION = By.XPATH, ".//button[text()='Зарегистрироваться']"  # Кнопка Зарегистрироваться
    SEARCH_ERROR_PASSWORD = By.XPATH, ".//p[text()='Некорректный пароль']"  # Предупреждение о некорректном пароле

    SEARCH_BUTTON_FILLINGS = By.XPATH, ".//span[text()='Начинки']"  # Кнопка Начинки
    SEARCH_BUTTON_SAUCES = By.XPATH, ".//span[text()='Соусы']"  # Кнопка Соусы
    SEARCH_BUTTON_BREADS = By.XPATH, ".//span[text()='Булки']"  # Кнопка Булки
    CHECK_SECTION_FILLINGS = By.XPATH, ".//h2[text()='Начинки']"  # Раздел Начинки
    CHECK_SECTION_SAUCES = By.XPATH, ".//h2[text()='Соусы']"  # Раздел Соусы
    CHECK_SECTION_BREADS = By.XPATH, ".//h2[text()='Булки']"  # Раздел Булки
