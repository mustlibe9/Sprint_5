import pytest
import random
import string
import locators
import urls
import data
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(urls.STELLAR_BURGERS_URL)

    yield driver

    driver.quit()


@pytest.fixture
def login_on_enter_form(driver):
    def login():
        email, password = data.REGISTERED_CREDENTIALS

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                locators.EMAIL_INPUT_LOGIN
            )
        ).send_keys(email)

        driver.find_element(*locators.PASSWORD_INPUT_LOGIN).send_keys(password)
        driver.find_element(*locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                locators.MAKE_ORDER_BUTTON
            )
        )

    return login


@pytest.fixture
def login_from_launch(driver, login_on_enter_form):
    def login():
        driver.find_element(*locators.LOGIN_ACCOUNT_BUTTON).click()
        login_on_enter_form()

    return login


@pytest.fixture
def go_to_account_page_from_launch(driver, login_from_launch):
    def go_to_account():
        login_from_launch()
        driver.find_element(*locators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                locators.ACCOUNT_PROFILE_LINK
            )
        ).click()

    return go_to_account


@pytest.fixture
def test_email():
    return f"test_user_{random.randint(100, 999)}_{random.randint(100, 999)}@yandex.ru"


@pytest.fixture
def test_password():
    letters_and_digits = string.ascii_letters + string.digits
    return "".join(random.choice(letters_and_digits) for _ in range(6))
