from selenium.webdriver.common.by import By


class AccountPageLocators:
    # Profile section
    PROFILE_BUTTON = (By.XPATH, "//a[text()='Профиль']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
    
    # Login form
    EMAIL_INPUT = (By.XPATH, "//input[@type='text' and @name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    
    # Registration form
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    
    # Navigation
    LOGO_LINK = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    
    # Error messages
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]")