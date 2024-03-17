from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators


class TestsLogin:

    def test_login_with_login_button(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        assert driver.find_element(*Locators.PLACE_ORDER_BUTTON).is_displayed()

    def test_login_with_personal_account_button(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_LOCATOR))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.BASE_USER.get("email"))
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.BASE_USER.get("password"))
        driver.find_element(*Locators.LOG_ON_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        assert driver.find_element(*Locators.PLACE_ORDER_BUTTON).is_displayed()

    def test_login_with_button_in_reg_form(self, driver):
        driver.get(Constants.REGISTRATION_URL)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REGISTRATION_LOCATOR))
        driver.find_element(*Locators.LOGIN_TEXT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_LOCATOR))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.BASE_USER.get("email"))
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.BASE_USER.get("password"))
        driver.find_element(*Locators.LOG_ON_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        assert driver.find_element(*Locators.PLACE_ORDER_BUTTON).is_displayed()

    def test_login_with_reset_password_button(self, driver):
        driver.get(Constants.FORGOT_PASSWORD_URL)
        driver.find_element(*Locators.LOGIN_TEXT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_LOCATOR))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.BASE_USER.get("email"))
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.BASE_USER.get("password"))
        driver.find_element(*Locators.LOG_ON_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        assert driver.find_element(*Locators.PLACE_ORDER_BUTTON).is_displayed()