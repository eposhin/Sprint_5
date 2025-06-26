import pytest
from selenium import webdriver
from curl import *
from locators import Locators
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.wait import WebDriverWait
from data import Credantial

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(main_site)
    yield driver
    driver.quit()

@pytest.fixture
def registration(driver):
    driver.find_element(*Locators.button_entrance_account).click()
    driver.find_element(*Locators.button_registration_entrance).click()
    return driver

@pytest.fixture
def authorization(driver):
    driver.find_element(*Locators.button_entrance_account).click() # ищу кнопку войти в аккаунт и клик
    driver.find_element(*Locators.field_email).send_keys(Credantial.email)  # заполняем поле email
    driver.find_element(*Locators.field_password).send_keys(Credantial.password)  # заполняем поле Пароль
    driver.find_element(*Locators.button_entrance_in_login_page).click()  # кликаем на Войти
    WebDriverWait(driver, 10).until(ES.visibility_of_element_located(Locators.place_order)) # жду загрузки кнопки оформить заказ
    driver.find_element(*Locators.button_private_area).click()  # кликаю Личный кабинет
    WebDriverWait(driver, 10).until(ES.visibility_of_element_located(Locators.button_exit))  # жду кнопки Выход
    return driver
