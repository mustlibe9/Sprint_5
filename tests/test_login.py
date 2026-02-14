from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators as locators


class TestLogin:

    def test_login_from_main_page_successful(self, driver, login_on_enter_form):
        driver.find_element(*locators.LOGIN_ACCOUNT_BUTTON).click()
        login_on_enter_form()

        assert driver.find_element(*locators.MAKE_ORDER_BUTTON).is_displayed()

    def test_login_from_account_successful(self, driver, login_on_enter_form):
        driver.find_element(*locators.ACCOUNT_LINK).click()
        login_on_enter_form()

        assert driver.find_element(*locators.MAKE_ORDER_BUTTON).is_displayed()

    def test_login_from_registration_successful(self, driver, login_on_enter_form):
        driver.find_element(*locators.LOGIN_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 1).until(
            expected_conditions.visibility_of_element_located(locators.REGISTER_LINK)
        ).click()

        WebDriverWait(driver, 1).until(
            expected_conditions.visibility_of_element_located(locators.LOGIN_LINK)
        ).click()

        login_on_enter_form()

        assert driver.find_element(*locators.MAKE_ORDER_BUTTON).is_displayed()

    def test_login_from_password_recovery_successful(self, driver, login_on_enter_form):
        driver.find_element(*locators.LOGIN_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 1).until(
            expected_conditions.visibility_of_element_located(
                locators.FORGOT_PASSWORD_LINK
            )
        ).click()

        WebDriverWait(driver, 1).until(
            expected_conditions.visibility_of_element_located(locators.LOGIN_LINK)
        ).click()

        login_on_enter_form()

        assert driver.find_element(*locators.MAKE_ORDER_BUTTON).is_displayed()
