import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators_personal_account_transition import TestLocatorsPersonalAccountTransition


class TestPersonalAccountTransition:
    def test_click_personal_account_transition(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*TestLocatorsPersonalAccountTransition.SEARCH_BUTTON_LOGIN_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocatorsPersonalAccountTransition.SEARCH_BUTTON_LOGIN))

        driver.find_element(*TestLocatorsPersonalAccountTransition.SEARCH_INPUT_EMAIL).send_keys(
            'irina_anokhina9826@yandex.ru')
        driver.find_element(*TestLocatorsPersonalAccountTransition.SEARCH_INPUT_PASSWORD).send_keys(
            '11223344')

        driver.find_element(*TestLocatorsPersonalAccountTransition.CLICK_BUTTON_LOGIN).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located
                                       (TestLocatorsPersonalAccountTransition.SEARCH_BUTTON_PERSONAL_ACCOUNT))

        driver.find_element(*TestLocatorsPersonalAccountTransition.SEARCH_BUTTON_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located
                                       (TestLocatorsPersonalAccountTransition.SEARCH_TEXT_PROFILE))

        driver.quit()
