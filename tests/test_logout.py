from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestsLogout:

    def test_logout_with_authorize(self, login):
        driver = login
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ACCOUNT_TEXT_LOCATOR))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_LOCATOR))
        assert driver.find_element(*Locators.LOGIN_LOCATOR).is_displayed()