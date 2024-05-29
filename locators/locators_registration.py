from selenium.webdriver.common.by import By


class TestLocatorsRegistration:
    SEARCH_INPUT_NAME = By.XPATH, ".//*[text()='Имя']/following-sibling::input"  # Поле для ввода имени
    SEARCH_INPUT_EMAIL = By.XPATH, ".//*[text()='Email']/following-sibling::input"  # Поле для ввода email
    SEARCH_INPUT_PASSWORD = By.XPATH, ".//*[text()='Пароль']/following-sibling::input"  # Поле для ввода пароля
    CHECK_BUTTON_REGISTRATION = By.XPATH, ".//button[text()='Зарегистрироваться']"  # Кнопка Зарегистрироваться
    SEARCH_BUTTON_LOGIN = By.XPATH, ".//h2[text()='Вход']"  # Кнопка Вход
    SEARCH_ERROR_PASSWORD = By.XPATH, ".//p[text()='Некорректный пароль']"  # Предупреждение о некорректном пароле
