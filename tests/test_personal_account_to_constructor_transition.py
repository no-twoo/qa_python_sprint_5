from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators_personal_account_to_constructor_transition import (
    TestLocatorsPersonalAccountToConstructorTransition)


class TestPersonalAccountToConstructorTransition:
    def test_click_conctructor(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')

        driver.find_element(*TestLocatorsPersonalAccountToConstructorTransition.SEARCH_BUTTON_LOGIN_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located
            (TestLocatorsPersonalAccountToConstructorTransition.SEARCH_BUTTON_LOGIN))

        driver.find_element(*TestLocatorsPersonalAccountToConstructorTransition.SEARCH_INPUT_EMAIL).send_keys(
            'irina_anokhina9826@yandex.ru')
        driver.find_element(*TestLocatorsPersonalAccountToConstructorTransition.SEARCH_INPUT_PASSWORD).send_keys(
            '11223344')

        driver.find_element(*TestLocatorsPersonalAccountToConstructorTransition.CLICK_BUTTON_LOGIN).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located
                                       (TestLocatorsPersonalAccountToConstructorTransition.
                                        SEARCH_BUTTON_PERSONAL_ACCOUNT))

        driver.find_element(*TestLocatorsPersonalAccountToConstructorTransition.SEARCH_BUTTON_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located
                                       (TestLocatorsPersonalAccountToConstructorTransition.SEARCH_TEXT_PROFILE))

        driver.find_element(*TestLocatorsPersonalAccountToConstructorTransition.SEARCH_BUTTON_CONSTRUCTOR).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located
            (TestLocatorsPersonalAccountToConstructorTransition.SEARCH_BUTTON_ORDER))

        driver.quit()

    def test_click_logo(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')

        driver.find_element(*TestLocatorsPersonalAccountToConstructorTransition.SEARCH_BUTTON_LOGIN_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located
            (TestLocatorsPersonalAccountToConstructorTransition.SEARCH_BUTTON_LOGIN))

        driver.find_element(*TestLocatorsPersonalAccountToConstructorTransition.SEARCH_INPUT_EMAIL).send_keys(
            'irina_anokhina9826@yandex.ru')

        driver.find_element(*TestLocatorsPersonalAccountToConstructorTransition.SEARCH_INPUT_PASSWORD).send_keys(
            '11223344')

        driver.find_element(*TestLocatorsPersonalAccountToConstructorTransition.CLICK_BUTTON_LOGIN).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located
                                       (TestLocatorsPersonalAccountToConstructorTransition.
                                        SEARCH_BUTTON_PERSONAL_ACCOUNT))

        driver.find_element(*TestLocatorsPersonalAccountToConstructorTransition.SEARCH_BUTTON_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located
                                       (TestLocatorsPersonalAccountToConstructorTransition.SEARCH_TEXT_PROFILE))

        driver.find_element(*TestLocatorsPersonalAccountToConstructorTransition.SEARCH_BUTTON_LOGO).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located
            (TestLocatorsPersonalAccountToConstructorTransition.SEARCH_BUTTON_ORDER))

        driver.quit()
