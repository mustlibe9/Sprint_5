from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators as locators


class TestAccount:

    def test_account_enter(self, driver, go_to_account_page_from_launch):
        go_to_account_page_from_launch()

        assert "/account/profile" in driver.current_url

    def test_account_to_constructor(self, driver, go_to_account_page_from_launch):
        go_to_account_page_from_launch()

        driver.find_element(*locators.CONSTRUCTOR_LINK).click()

        constructor_header = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                locators.CONSTRUCTOR_HEADER
            )
        )

        assert constructor_header.is_displayed()

    def test_account_to_constructor_by_logo(
        self, driver, go_to_account_page_from_launch
    ):
        go_to_account_page_from_launch()

        driver.find_element(*locators.LOGO_LINK).click()

        constructor_header = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                locators.CONSTRUCTOR_HEADER
            )
        )

        assert constructor_header.is_displayed()

    def test_account_exit(self, driver, go_to_account_page_from_launch):
        go_to_account_page_from_launch()

        driver.find_element(*locators.LOGOUT_BUTTON).click()

        assert WebDriverWait(driver, 3).until(
            expected_conditions.url_contains("/login")
        )
