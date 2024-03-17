from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestsRegistrations:

    def test_registration_with_correct_data(self, driver, correct_user_data):
        driver.find_element(*Locators.LOG_INTO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_LOCATOR))
        driver.find_element(*Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REGISTRATION_LOCATOR))
        driver.find_element(*Locators.NAME_INPUT).send_keys(correct_user_data.get("name"))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(correct_user_data.get("email"))
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(correct_user_data.get("password"))
        driver.find_element(*Locators.REGISTRATION_BUTTON_ON_REG_PAGE).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_LOCATOR))
        assert driver.find_element(*Locators.LOGIN_LOCATOR).is_displayed()

    def test_registration_with_incorrect_password(self, driver, incorrect_user_data):
        driver.find_element(*Locators.LOG_INTO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_LOCATOR))
        driver.find_element(*Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REGISTRATION_LOCATOR))
        driver.find_element(*Locators.NAME_INPUT).send_keys(incorrect_user_data.get("name"))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(incorrect_user_data.get("email"))
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(incorrect_user_data.get("password"))
        driver.find_element(*Locators.REGISTRATION_BUTTON_ON_REG_PAGE).click()
        assert driver.find_element(*Locators.INCORRECT_PASSWORD_LOCATOR).is_displayed()
