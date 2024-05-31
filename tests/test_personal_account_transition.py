from conftest import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import TestLocators
from data import *


class TestPersonalAccountTransition:
    def test_click_personal_account_transition(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*TestLocators.SEARCH_BUTTON_LOGIN_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_BUTTON_LOGIN))

        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(login_email)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD).send_keys(login_password)

        driver.find_element(*TestLocators.CLICK_BUTTON_LOGIN).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located
                                       (TestLocators.SEARCH_BUTTON_PERSONAL_ACCOUNT))

        driver.find_element(*TestLocators.SEARCH_BUTTON_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located
                                       (TestLocators.SEARCH_TEXT_PROFILE))

        check_text = driver.find_element(*TestLocators.SEARCH_TEXT_PROFILE).text

        assert check_text == "Профиль"
