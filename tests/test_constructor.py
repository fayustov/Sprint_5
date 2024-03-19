from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestsConstructor:

    def test_switch_to_buns_in_constructor(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BURGER_INGREDIENTS_CONTAINER))
        driver.find_element(*Locators.TOPPINGS_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.TOPPINGS_LIST))
        driver.find_element(*Locators.BUNS_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BUNS_LIST))
        assert driver.find_element(*Locators.BUNS_LIST).is_displayed()

    def test_switch_to_sauces_in_constructor(self, driver):
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.SAUCES_LIST))
        assert driver.find_element(*Locators.SAUCES_LIST).is_displayed()

    def test_switch_to_toppings_in_constructor(self, driver):
        driver.find_element(*Locators.TOPPINGS_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.TOPPINGS_LIST))
        assert driver.find_element(*Locators.TOPPINGS_LIST).is_displayed()
