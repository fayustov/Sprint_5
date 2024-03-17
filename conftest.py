import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from constants import Constants
from locators import Locators


@pytest.fixture(scope='function')
def driver():
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(Constants.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def login(driver):
    driver.find_element(*Locators.LOG_INTO_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.BASE_USER.get("email"))
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.BASE_USER.get("password"))
    driver.find_element(*Locators.LOG_ON_BUTTON).click()
    return driver


@pytest.fixture()
def correct_user_data():
    fake = Faker()
    name = fake.name()
    email = fake.email()
    password = fake.password()
    return {"name": name, "email": email, "password": password}


@pytest.fixture()
def incorrect_user_data():
    return {"name": "Имя", "email": "test@email.com", "password": "12345"}
