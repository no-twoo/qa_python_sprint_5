from selenium.webdriver.common.by import By


class TestLocatorsSectionConstructor:
    SEARCH_BUTTON_FILLINGS = By.XPATH, ".//span[text()='Начинки']"  # Кнопка Начинки
    SEARCH_BUTTON_SAUCES = By.XPATH, ".//span[text()='Соусы']"  # Кнопка Соусы
    SEARCH_BUTTON_BREADS = By.XPATH, ".//span[text()='Булки']"  # Кнопка Булки
    CHECK_SECTION_FILLINGS = By.XPATH, ".//h2[text()='Начинки']"  # Раздел Начинки
    CHECK_SECTION_SAUCES = By.XPATH, ".//h2[text()='Соусы']"  # Раздел Соусы
    CHECK_SECTION_BREADS = By.XPATH, ".//h2[text()='Булки']"  # Раздел Булки
