from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
from locators import *

#Login пользователя
def test_login_success_shows_homepage(driver, random_email, test_password = 'Test1234'):
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

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PROFILE_BUTTON))

#Выйти из ЛК пользователя
    driver.find_element(*LOGOUT_BUTTON).click()
    WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(LOGIN_AND_REGISTRATION_BUTTON))

#Нажать кнопку «Вход и регистрация».
    driver.find_element(*LOGIN_AND_REGISTRATION_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(POPUP_LOGIN_HEADER))

#Заполнить все поля формы авторизации и нажать кнопку «Войти».
    driver.find_element(*EMAIL_INPUT).clear()
    driver.find_element(*EMAIL_INPUT).send_keys(new_email)
    driver.find_element(*PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LOGIN_BUTTON).click()

#Проверить: произошёл переход на главную страницу, в правом верхнем углу отображается аватар пользователя и имя User.
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PROFILE_BUTTON))
    assert driver.find_element(*USERNAME).text == 'User.'
    
    driver.quit()


#Logout пользователя
def  test_logout_hides_user_info(driver, random_email, test_password = 'Test1234'):
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

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PROFILE_BUTTON))

#Выйти из ЛК пользователя
    driver.find_element(*LOGOUT_BUTTON).click()
    WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(LOGIN_AND_REGISTRATION_BUTTON))

#Нажать кнопку «Вход и регистрация».
    driver.find_element(*LOGIN_AND_REGISTRATION_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(POPUP_LOGIN_HEADER))

#Заполнить все поля формы авторизации и нажать кнопку «Войти».
    driver.find_element(*EMAIL_INPUT).clear()
    driver.find_element(*EMAIL_INPUT).send_keys(new_email)
    driver.find_element(*PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PROFILE_BUTTON))

#Нажать кнопку «Выйти».
    driver.find_element(*LOGOUT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.invisibility_of_element_located(PROFILE_BUTTON))
    WebDriverWait(driver, 3).until(expected_conditions.invisibility_of_element_located(USERNAME))
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LOGIN_AND_REGISTRATION_BUTTON))

#Проверить: аватар пользователя и имя User больше не отображается в правом верхнем углу около кнопки «Разместить объявление», 
# там теперь отображается кнопка «Вход и регистрация».
    is_visible_profile = driver.find_elements(*PROFILE_BUTTON)
    is_visible_username = driver.find_elements(*USERNAME)
    is_visible_login_button = driver.find_elements(*LOGIN_AND_REGISTRATION_BUTTON)
    assert (len(is_visible_profile) == 0
            and len(is_visible_username) == 0
            and len(is_visible_login_button) == 1)

    driver.quit()
