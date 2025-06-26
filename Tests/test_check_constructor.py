# Проверка функциональности раздела «Конструктор»
import pytest
from locators import Locators
from Tests.conftest import driver

class TestCheckConstructor:

    @pytest.mark.parametrize("element_locator, expected_text", [
        (Locators.inscription_souse, "Соусы"),
        (Locators.inscription_filling, "Начинки"),
        (Locators.inscription_bread, "Булки")
    ])
    def test_check_crossing_constructor_sections(self, driver, element_locator, expected_text):
        driver.find_element(*Locators.link_construction).click()

        if expected_text == "Булки":
            driver.find_element(*Locators.inscription_filling).click()

        driver.find_element(*element_locator).click()
        assert driver.find_element(*element_locator).is_displayed() and \
               driver.find_element(*Locators.active_element_constructor).text == expected_text