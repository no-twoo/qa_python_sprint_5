from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators_login import TestLocatorsLogin


class TestLogin:
    def test_log_in_main(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*TestLocatorsLogin.SEARCH_BUTTON_LOGIN_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocatorsLogin.SEARCH_BUTTON_LOGIN))

        driver.find_element(*TestLocatorsLogin.SEARCH_INPUT_EMAIL).send_keys('irina_anokhina9826@yandex.ru')
        driver.find_element(*TestLocatorsLogin.SEARCH_INPUT_PASSWORD).send_keys('11223344')
        driver.find_element(*TestLocatorsLogin.CLICK_BUTTON_LOGIN).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocatorsLogin.SEARCH_BUTTON_ORDER))

        driver.quit()

    def test_log_in_personal_account(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*TestLocatorsLogin.SEARCH_BUTTON_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocatorsLogin.SEARCH_BUTTON_LOGIN))

        driver.find_element(*TestLocatorsLogin.SEARCH_INPUT_EMAIL).send_keys('irina_anokhina9826@yandex.ru')
        driver.find_element(*TestLocatorsLogin.SEARCH_INPUT_PASSWORD).send_keys('11223344')
        driver.find_element(*TestLocatorsLogin.CLICK_BUTTON_LOGIN).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocatorsLogin.SEARCH_BUTTON_ORDER))

        driver.quit()

    def test_log_in_registration_form(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*TestLocatorsLogin.CHECK_BUTTON_LOGIN).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocatorsLogin.SEARCH_BUTTON_LOGIN))

        driver.find_element(*TestLocatorsLogin.SEARCH_INPUT_EMAIL).send_keys('irina_anokhina9826@yandex.ru')
        driver.find_element(*TestLocatorsLogin.SEARCH_INPUT_PASSWORD).send_keys('11223344')
        driver.find_element(*TestLocatorsLogin.CLICK_BUTTON_LOGIN).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocatorsLogin.SEARCH_BUTTON_ORDER))

        driver.quit()

    def test_log_in_password_recovery_form(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        driver.find_element(*TestLocatorsLogin.CHECK_BUTTON_LOGIN).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocatorsLogin.SEARCH_BUTTON_LOGIN))

        driver.find_element(*TestLocatorsLogin.SEARCH_INPUT_EMAIL).send_keys('irina_anokhina9826@yandex.ru')
        driver.find_element(*TestLocatorsLogin.SEARCH_INPUT_PASSWORD).send_keys('11223344')
        driver.find_element(*TestLocatorsLogin.CLICK_BUTTON_LOGIN).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocatorsLogin.SEARCH_BUTTON_ORDER))

        driver.quit()
