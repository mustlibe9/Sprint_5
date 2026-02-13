from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators as locators


def test_login_from_main_page_successful(driver, login_on_enter_form):
    driver.find_element(*locators.LOGIN_ACCOUNT_BUTTON).click()
    login_on_enter_form()

    assert is_make_order_button_displayed(driver)


def test_login_from_account_successful(driver, login_on_enter_form):
    driver.find_element(*locators.ACCOUNT_LINK).click()
    login_on_enter_form()

    assert is_make_order_button_displayed(driver)


def test_login_from_registration_successful(driver, login_on_enter_form):
    driver.find_element(*locators.LOGIN_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 1).until(
        expected_conditions.visibility_of_element_located(locators.REGISTER_LINK)
    ).click()

    WebDriverWait(driver, 1).until(
        expected_conditions.visibility_of_element_located(locators.LOGIN_LINK)
    ).click()

    login_on_enter_form()

    assert is_make_order_button_displayed(driver)


def test_login_from_password_recovery_successful(driver, login_on_enter_form):
    driver.find_element(*locators.LOGIN_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 1).until(
        expected_conditions.visibility_of_element_located(locators.FORGOT_PASSWORD_LINK)
    ).click()

    WebDriverWait(driver, 1).until(
        expected_conditions.visibility_of_element_located(locators.LOGIN_LINK)
    ).click()

    login_on_enter_form()

    assert is_make_order_button_displayed(driver)


def is_make_order_button_displayed(driver):
    return driver.find_element(*locators.MAKE_ORDER_BUTTON).is_displayed()
