from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators as locators
import data


class TestRegistration:

    def test_registration_successful(self, driver, test_email, test_password):

        driver.find_element(*locators.LOGIN_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 1).until(
            expected_conditions.visibility_of_element_located(locators.REGISTER_LINK)
        ).click()

        driver.find_element(*locators.NAME_INPUT_REGISTER).send_keys(
            data.TEST_USER_NAME
        )
        driver.find_element(*locators.EMAIL_INPUT_REGISTER).send_keys(test_email)
        driver.find_element(*locators.PASSWORD_INPUT_REGISTER).send_keys(test_password)

        driver.find_element(*locators.REGISTER_BUTTON).click()

        assert WebDriverWait(driver, 3).until(
            expected_conditions.url_contains("/login")
        )

    def test_registration_incorrect_password_error(self, driver, test_email):

        driver.find_element(*locators.LOGIN_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 1).until(
            expected_conditions.visibility_of_element_located(locators.REGISTER_LINK)
        ).click()

        driver.find_element(*locators.NAME_INPUT_REGISTER).send_keys(
            data.TEST_USER_NAME
        )
        driver.find_element(*locators.EMAIL_INPUT_REGISTER).send_keys(test_email)

        driver.find_element(*locators.PASSWORD_INPUT_REGISTER).send_keys(
            data.INCORRECT_SHORT_PASSWORD
        )

        driver.find_element(*locators.REGISTER_BUTTON).click()

        error = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.PASSWORD_ERROR)
        )

        assert error.is_displayed()
