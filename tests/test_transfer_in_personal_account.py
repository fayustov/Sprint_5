from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestsTransferInPersonalAccount:

    def test_transfer_in_personal_account_without_authorization(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_LOCATOR))
        assert driver.find_element(*Locators.LOGIN_LOCATOR).is_displayed()

    def test_transfer_in_personal_account_with_authorization(self, login):
        driver = login
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ACCOUNT_TEXT_LOCATOR))
        assert driver.find_element(*Locators.ACCOUNT_TEXT_LOCATOR).is_displayed()
