from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators_logout import TestLocatorsLogout


class TestLogout:
    def test_log_out(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*TestLocatorsLogout.SEARCH_BUTTON_LOGIN_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocatorsLogout.SEARCH_BUTTON_LOGIN))

        driver.find_element(*TestLocatorsLogout.SEARCH_INPUT_EMAIL).send_keys('irina_anokhina9826@yandex.ru')
        driver.find_element(*TestLocatorsLogout.SEARCH_INPUT_PASSWORD).send_keys('11223344')
        driver.find_element(*TestLocatorsLogout.CLICK_BUTTON_LOGIN).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located
                                       (TestLocatorsLogout.SEARCH_BUTTON_PERSONAL_ACCOUNT))

        driver.find_element(*TestLocatorsLogout.SEARCH_BUTTON_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located
                                       (TestLocatorsLogout.SEARCH_TEXT_PROFILE))

        driver.find_element(*TestLocatorsLogout.SEARCH_BUTTON_LOGOUT).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocatorsLogout.SEARCH_BUTTON_LOGIN))

        driver.quit()
