from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestsTransferFromPersonalAccountToConstructor:

    def test_transfer_from_personal_account_to_constructor_with_constructor_button(self, login):
        driver = login
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.BUILD_A_BURGER_LOCATOR))
        assert driver.find_element(*Locators.BUILD_A_BURGER_LOCATOR)

    def test_transfer_from_personal_account_to_constructor_with_stellar_burgers_logo(self, login):
        driver = login
        driver.find_element(*Locators.STELLAR_BURGER_LOGO).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.BUILD_A_BURGER_LOCATOR))
        assert driver.find_element(*Locators.BUILD_A_BURGER_LOCATOR)
