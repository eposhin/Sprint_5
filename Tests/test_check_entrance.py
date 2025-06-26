# Проверки функциональности кнопок "Вход":
import pytest
from locators import Locators
from curl import *
from data import Credantial
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES


class TestCheckButtonEntranceInAccount:
    def test_entrance_button_in_main_page(self, driver):
        driver.find_element(*Locators.button_entrance_account).click()
        assert driver.current_url == login_site

class TestCheckButtonEntranceInPrivateArea:
    def test_entrance_button_in_private_page(self, driver):
        driver.find_element(*Locators.button_private_area).click()
        driver.find_element(*Locators.field_email).send_keys(Credantial.email)
        driver.find_element(*Locators.field_password).send_keys(Credantial.password)
        driver.find_element(*Locators.button_entrance_in_login_page).click()
        WebDriverWait(driver, 10).until(ES.visibility_of_element_located(Locators.place_order))
        driver.find_element(*Locators.button_private_area).click()
        assert driver.current_url == account_site

@pytest.mark.usefixtures("registration")
class TestCheckButtonEntranceInRegistration:
    def test_entrance_button_in_registration(self, driver):
        driver.find_element(*Locators.link_entrance_registration).click()
        assert driver.current_url == login_site

class TestCheckButtonEntranceInRecovery:
    def test_entrance_button_in_recovery_page(self, driver):
        driver.find_element(*Locators.button_entrance_account).click()
        driver.find_element(*Locators.link_recovery_password).click()
        driver.find_element(*Locators.link_entrance_forget_password).click()
        assert driver.current_url == login_site