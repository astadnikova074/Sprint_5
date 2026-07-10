from selenium.webdriver.common.by import By

URL ="https://qa-desk.education-services.ru/"

# Кнопка «Вход и регистрация»
LOGIN_AND_REGISTRATION_BUTTON = (By.XPATH, "//div[@class='header_flexRow__Xdqv1']/button[text()='Вход и регистрация']")

# Модальное окно регистрации (название)
POPUP_LOGIN_HEADER = (By.XPATH, "//div[@class='popUp_titleRow__M7tGg']//h1")

# Кнопка «Нет аккаунта»
NO_ACCOUNT_BUTTON = (By.XPATH, "//div[@class='popUp_buttonRow__+W8JD']/button[text()='Нет аккаунта']")

# Кнопка «Войти»
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

# Кнопка «Разместить объявление»
AD_POST_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")

# Форма регистрации
EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
SUBMIT_PASSWORD_INPUT = (By.XPATH, "//input[@name='submitPassword']")

EMAIL_PARENT = (By.XPATH, "//input[@name='email']/..")
PASSWORD_PARENT = (By.XPATH, "//input[@name='password']/..")
SUBMIT_PASSWORD_PARENT = (By.XPATH, "//input[@name='submitPassword']/..")

# Ошибка валидации
EMAIL_ERROR = (By.XPATH,"(//span[@class='input_span__yWPqB'])[1]")
# Красная рамка для полей
ERROR_INPUT_CLASS = "input_inputError__fLUP9"

# Кнопка «Создать аккаунт»
SUBMIT_BUTTON = (By.XPATH, "//div[@class='popUp_buttonRow__+W8JD']/button[text()='Создать аккаунт']")

# Авторизованная зона

#я хочу купить...
FILTER_HOMEPAGE = (By.XPATH, "//div[@class='input_inputDefaultSearch__EKhe3']")

# Кнопка профиля
PROFILE_BUTTON = (By.XPATH, "//button[@class='circleSmall']")

#Мои объявления
MY_ADS_HEADER = (By.XPATH, "//h1[text()='Мои объявления']")
AD_NAME = (By.XPATH, "//div[@class='about']//h2")
AD_CITY = (By.XPATH, "//div[@class='about']//h3")
AD_PRICE = (By.XPATH, "//div[@class='price']//h2")

# Имя пользователя
USERNAME = (By.XPATH, "//div[@class='flexRow']//h3")

# Кнопка "Выйти"
LOGOUT_BUTTON = (By.XPATH, "//div[@class='flexRow']//button[text()='Выйти']")

# Создание заявки
NAME_INPUT = (By.XPATH, "//input[@name='name']")
DESCRIPTION_INPUT = (By.XPATH, "//textarea[@name='description']")
PRICE_INPUT = (By.XPATH, "//input[@name='price']")
DROP_DOWN_CATEGORY = (By.XPATH, "//input[@name='category']/../button")
DROP_DOWN_CITY = (By.XPATH, "//input[@name='city']/../button")
SUBMIT_BUTTON_AD = (By.XPATH, "//button[@type= 'submit']")

#Получить состояние товара
def get_condition(condition):
    return (By.XPATH, f"//label[text()='{condition}']/../div")

#Получить локатор для города или категории
def get_locator(name):
    return (By.XPATH, f"//span[text()='{name}']")


