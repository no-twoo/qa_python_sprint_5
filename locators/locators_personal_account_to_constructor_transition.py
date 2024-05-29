from selenium.webdriver.common.by import By


class TestLocatorsPersonalAccountToConstructorTransition:
    SEARCH_BUTTON_LOGIN_ACCOUNT = By.XPATH, ".//button[text()='Войти в аккаунт']"  # Кнопка войти в аккаунт
    SEARCH_BUTTON_LOGIN = By.XPATH, ".//h2[text()='Вход']"  # Кнопка Вход
    SEARCH_INPUT_EMAIL = By.XPATH, ".//*[text()='Email']/following-sibling::input"  # Поле для ввода email
    SEARCH_INPUT_PASSWORD = By.XPATH, ".//*[text()='Пароль']/following-sibling::input"  # Поле для ввода пароля
    CLICK_BUTTON_LOGIN = By.XPATH, ".//button[text()='Войти']"  # Кнопка Войти
    SEARCH_BUTTON_PERSONAL_ACCOUNT = By.XPATH, ".//*[text()='Личный Кабинет']"  # Кнопка Личный кабинет
    SEARCH_TEXT_PROFILE = By.XPATH, ".//a[text()='Профиль']"  # Кнопка Профиль
    SEARCH_BUTTON_CONSTRUCTOR = By.XPATH, ".//p[text()='Конструктор']"  # Кнопка Конструктор
    SEARCH_BUTTON_ORDER = By.XPATH, ".//button[text()='Оформить заказ']"  # Кнопка Оформить заказ
    SEARCH_BUTTON_LOGO = By.XPATH, ".//*[contains(@class, 'AppHeader_header__logo')]"  # Картинка логотипа