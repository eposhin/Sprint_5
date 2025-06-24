# Проверка Регистрации:
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
from locators import Locators
from curl import *
from generator_lp import GenerationEmailPassword
import random
import string

# Успешная регистрация.
@pytest.mark.usefixtures("registration")
class TestNewCorrectRegistration:
    def test_correct_registration(self, driver):
        generator = GenerationEmailPassword()
        generate_name, generate_email, generate_password = generator.generate_login()
        driver.find_element(*Locators.registration_name).send_keys(generate_name)
        driver.find_element(*Locators.registration_email).send_keys(generate_email)
        driver.find_element(*Locators.registration_password).send_keys(generate_password)
        driver.find_element(*Locators.button_registration_register).click()
        WebDriverWait(driver, 10).until(es.visibility_of_element_located(Locators.button_entrance_in_login_page))
        driver.find_element(*Locators.field_email).send_keys(generate_email)
        driver.find_element(*Locators.field_password).send_keys(generate_password)
        driver.find_element(*Locators.button_entrance_in_login_page).click()
        WebDriverWait(driver, 3).until(es.visibility_of_element_located(Locators.place_order))
        driver.find_element(*Locators.button_private_area).click()
        WebDriverWait(driver, 3).until(es.visibility_of_element_located(Locators.button_exit))
        assert driver.current_url == profile_site

# Поле «Имя» не должно быть пустым
@pytest.mark.usefixtures("registration")
class TestNonameRegistration:
    def test_noname_registration(self, driver):
        generator = GenerationEmailPassword()
        generate_name, generate_email, generate_password = generator.generate_login()
        driver.find_element(*Locators.registration_name).send_keys('')
        driver.find_element(*Locators.registration_email).send_keys(generate_email)
        driver.find_element(*Locators.registration_password).send_keys(generate_password)
        driver.find_element(*Locators.button_registration_register).click()
        assert driver.current_url == register_site

# Минимальный пароль — шесть символов.
@pytest.mark.usefixtures("registration")
class TestShortPassword:
    def test_short_password_registration(self, driver):
        generator = GenerationEmailPassword()
        generate_name, generate_email, _ = generator.generate_login()
        password_length = random.randint(1, 5)
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))
        short_password = f"{random_string}"
        driver.find_element(*Locators.registration_name).send_keys(generate_name)
        driver.find_element(*Locators.registration_email).send_keys(generate_email)
        driver.find_element(*Locators.registration_password).send_keys(short_password)
        driver.find_element(*Locators.button_registration_register).click()
        error_text =  driver.find_element(*Locators.no_correct_password).text
        assert error_text == "Некорректный пароль"