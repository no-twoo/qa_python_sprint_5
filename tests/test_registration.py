import random

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators_registration import TestLocatorsRegistration


class TestRegistration:

    def test_registration_successful(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocatorsRegistration.SEARCH_INPUT_NAME).send_keys(
            'Ирина')
        new_email = f"irina_anokhina9{random.randint(100, 999)}@yandex.ru"
        driver.find_element(*TestLocatorsRegistration.SEARCH_INPUT_EMAIL).send_keys(
            new_email)
        driver.find_element(*TestLocatorsRegistration.SEARCH_INPUT_PASSWORD).send_keys(
            '11223344')
        driver.find_element(*TestLocatorsRegistration.CHECK_BUTTON_REGISTRATION).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located
                                       (TestLocatorsRegistration.SEARCH_BUTTON_LOGIN))

        driver.quit()

    def test_password_error(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocatorsRegistration.SEARCH_INPUT_NAME).send_keys(
            'Ирина')
        new_email = f"irina_anokhina9{random.randint(100, 999)}@yandex.ru"
        driver.find_element(*TestLocatorsRegistration.SEARCH_INPUT_EMAIL).send_keys(new_email)
        driver.find_element(*TestLocatorsRegistration.SEARCH_INPUT_PASSWORD).send_keys(
            '123')
        driver.find_element(*TestLocatorsRegistration.CHECK_BUTTON_REGISTRATION).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocatorsRegistration.SEARCH_ERROR_PASSWORD))

        driver.quit()
