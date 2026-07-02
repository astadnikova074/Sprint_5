from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
from locators import *

class TestRegistration:
    #Регистрация пользователя
    def test_registration_user_opened_homepage(self, driver, random_email, test_password = 'Test1234'):
        new_email = random_email
        password = test_password
        submit_password = test_password

    #Перейти на стенд
        driver.get(URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LOGIN_AND_REGISTRATION_BUTTON))

    #Нажать кнопку «Вход и регистрация».
        driver.find_element(*LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(POPUP_LOGIN_HEADER))

    #Нажать кнопку «Нет аккаунта».
        driver.find_element(*NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(EMAIL_INPUT))

    #Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт».
        driver.find_element(*EMAIL_INPUT).clear()
        driver.find_element(*EMAIL_INPUT).send_keys(new_email)
        driver.find_element(*PASSWORD_INPUT).send_keys(password)
        driver.find_element(*SUBMIT_PASSWORD_INPUT).send_keys(submit_password)
        driver.find_element(*SUBMIT_BUTTON).click()

    #Проверить: произошёл переход на главную страницу, отображается аватар пользователя и имя User.
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PROFILE_BUTTON))
        assert driver.find_element(*USERNAME).text == 'User.'
        driver.quit()

    #Регистрация пользователя c email не по маске  *******@*******.***
    @pytest.mark.parametrize("email", ['test.ru','test@test'])
    def test_registration_user_with_invalid_email_shows_error(self, driver, email):
        new_email = email

    #Перейти на стенд
        driver.get(URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LOGIN_AND_REGISTRATION_BUTTON))

    #Нажать кнопку «Вход и регистрация».
        driver.find_element(*LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(POPUP_LOGIN_HEADER))

    #Нажать кнопку «Нет аккаунта».
        driver.find_element(*NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(EMAIL_INPUT))

    #Заполнить поле Email формы регистрации и нажать кнопку «Создать аккаунт».
        driver.find_element(*EMAIL_INPUT).clear()
        driver.find_element(*EMAIL_INPUT).send_keys(new_email)
        driver.find_element(*SUBMIT_BUTTON).click()

    #Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email отображается сообщение «Ошибка».
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(EMAIL_ERROR))
        email_error_text = driver.find_element(*EMAIL_ERROR).text

        assert (
            ERROR_INPUT_CLASS == driver.find_element(*EMAIL_PARENT).get_attribute("class") 
            and ERROR_INPUT_CLASS == driver.find_element(*PASSWORD_PARENT).get_attribute("class") 
            and ERROR_INPUT_CLASS == driver.find_element(*SUBMIT_PASSWORD_PARENT).get_attribute("class") 
            and email_error_text == 'Ошибка'
        )
        driver.quit()

    #Регистрация уже существующего пользователя
    def test_registration_with_existing_email_shows_error(self, driver, random_email, test_password = 'Test1234'):

    #Перейти на стенд
        driver.get(URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LOGIN_AND_REGISTRATION_BUTTON))

    #Регистрация нового пользователя
        new_email = random_email
        password = test_password
        submit_password = test_password

        driver.find_element(*LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(POPUP_LOGIN_HEADER))

        driver.find_element(*NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(EMAIL_INPUT))

        driver.find_element(*EMAIL_INPUT).clear()
        driver.find_element(*EMAIL_INPUT).send_keys(new_email)
        driver.find_element(*PASSWORD_INPUT).send_keys(password)
        driver.find_element(*SUBMIT_PASSWORD_INPUT).send_keys(submit_password)
        driver.find_element(*SUBMIT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(PROFILE_BUTTON))

    #Выйти из ЛК пользователя
        driver.find_element(*LOGOUT_BUTTON).click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(LOGIN_AND_REGISTRATION_BUTTON))

    #Регистрация нового пользователя с уже существующими данными
        driver.find_element(*LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(POPUP_LOGIN_HEADER))

        driver.find_element(*NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(EMAIL_INPUT))
    #Заполнить все поля формы регистрации данными уже существующего в системе пользователя и нажать кнопку «Создать аккаунт».
        driver.find_element(*EMAIL_INPUT).clear()
        driver.find_element(*EMAIL_INPUT).send_keys(new_email)
        driver.find_element(*PASSWORD_INPUT).send_keys(password)
        driver.find_element(*SUBMIT_PASSWORD_INPUT).send_keys(submit_password)
        driver.find_element(*SUBMIT_BUTTON).click()
    #Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email отображается сообщение «Ошибка».
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(EMAIL_ERROR))
        email_error_text = driver.find_element(*EMAIL_ERROR).text

        assert (
            ERROR_INPUT_CLASS == driver.find_element(*EMAIL_PARENT).get_attribute("class") 
            and ERROR_INPUT_CLASS == driver.find_element(*PASSWORD_PARENT).get_attribute("class") 
            and ERROR_INPUT_CLASS == driver.find_element(*SUBMIT_PASSWORD_PARENT).get_attribute("class") 
            and email_error_text == 'Ошибка'
        )

        driver.quit()
