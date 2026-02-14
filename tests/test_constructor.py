from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators as locators


class TestConstructor:

    def test_constructor_buns_tab_positioning(self, driver):

        driver.find_element(*locators.SAUCES_TAB).click()

        WebDriverWait(driver, 1).until(
            expected_conditions.visibility_of_element_located(locators.SAUCES_HEADER)
        )

        driver.find_element(*locators.BUNS_TAB).click()

        buns_header = WebDriverWait(driver, 1).until(
            expected_conditions.visibility_of_element_located(locators.BUNS_HEADER)
        )

        assert buns_header.is_displayed()

    def test_constructor_sauces_tab_positioning(self, driver):

        driver.find_element(*locators.SAUCES_TAB).click()

        sauces_header = WebDriverWait(driver, 1).until(
            expected_conditions.visibility_of_element_located(locators.SAUCES_HEADER)
        )

        assert sauces_header.is_displayed()

    def test_constructor_fillings_tab_positioning(self, driver):

        driver.find_element(*locators.FILLINGS_TAB).click()

        fillings_header = WebDriverWait(driver, 1).until(
            expected_conditions.visibility_of_element_located(locators.FILLINGS_HEADER)
        )

        assert fillings_header.is_displayed()
