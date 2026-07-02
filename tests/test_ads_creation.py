from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
from locators import *

class TestAdsCreation:

    #Создание объявления неавторизованным пользователем
    def test_create_ad_unauthorized_shows_auth_popup(self, driver):
    #Перейти на стенд
        driver.get(URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LOGIN_AND_REGISTRATION_BUTTON))

    #Нажать кнопку «Разместить объявление».
        driver.find_element(*AD_POST_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(POPUP_LOGIN_HEADER))

    #Проверить: отображается модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь».
        assert driver.find_element(*POPUP_LOGIN_HEADER).text == 'Чтобы разместить объявление, авторизуйтесь'

        driver.quit()

    #Создание объявления авторизованным пользователем
    @pytest.mark.parametrize("city, category, condition", [
        ("Москва", "Технологии", "Новый"),
        ("Санкт-Петербург", "Книги", "Б/У"),
        ("Новосибирск", "Авто", "Новый"),
        ("Екатеринбург", "Хобби", "Б/У"),
        ("Казань", "Садоводство", "Новый"),
    ])
    def test_create_ad_authorized_user(self, driver,random_email, ad_name, ad_description, ad_price, city, category, condition, test_password = 'Test1234'):
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

    #Нажать кнопку «Разместить объявление».
        driver.find_element(*AD_POST_BUTTON).click()

        element_name_input = driver.find_element(*NAME_INPUT)
        driver.execute_script("arguments[0].scrollIntoView();", element_name_input)

    #Заполнить все поля формы: «Название», «Описание товара», «Стоимость» — стоимость должна быть указана в числовом формате.
        name = ad_name
        description = ad_description
        price = ad_price
        driver.find_element(*NAME_INPUT).send_keys(name)
        driver.find_element(*DESCRIPTION_INPUT).send_keys(description)
        driver.find_element(*PRICE_INPUT).send_keys(price)

    #Выбрать из Dropdown «Категорию» и «Город».
        ad_category = category
        ad_city = city
        driver.find_element(*DROP_DOWN_CATEGORY).click()
        driver.find_element(*get_locator(ad_category)).click()
        
        driver.find_element(*DROP_DOWN_CITY).click()
        driver.find_element(*get_locator(ad_city)).click()

    #Выбрать RabioButton «Состояние товара».
        driver.find_element(*get_condition(condition)).click()

    #Нажать кнопку «Опубликовать».
        driver.find_element(*SUBMIT_BUTTON_AD).click()
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(FILTER_HOMEPAGE))

    #Перейти в профиль пользователя.
        WebDriverWait(driver,5).until(expected_conditions.element_to_be_clickable(PROFILE_BUTTON)).click()

    #Проверить: в блоке «Мои объявления» отображается созданное объявление.
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(MY_ADS_HEADER))

        element_name_input = driver.find_element(*MY_ADS_HEADER)
        driver.execute_script("arguments[0].scrollIntoView();", element_name_input)

        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(AD_CITY))
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(AD_NAME))
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(AD_PRICE))

        assert(
            driver.find_element(*AD_CITY).text == ad_city
            and driver.find_element(*AD_NAME).text == name
            and driver.find_element(*AD_PRICE).text.replace(" ", "") == str(price)+'₽'
        )

        driver.quit()
