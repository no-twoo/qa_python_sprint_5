from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators_section_constructor import TestLocatorsSectionConstructor


class TestSectionConstructor:
    def test_check_operation_of_transitions(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*TestLocatorsSectionConstructor.SEARCH_BUTTON_FILLINGS).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located
                                       (TestLocatorsSectionConstructor.CHECK_SECTION_FILLINGS))

        driver.find_element(*TestLocatorsSectionConstructor.SEARCH_BUTTON_SAUCES).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located
                                       (TestLocatorsSectionConstructor.CHECK_SECTION_SAUCES))

        driver.find_element(*TestLocatorsSectionConstructor.SEARCH_BUTTON_BREADS).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located
                                       (TestLocatorsSectionConstructor.CHECK_SECTION_BREADS))

        driver.quit()
