from selenium.webdriver.common.by import By

class AccountPageLocators:
    # Profile section
    PROFILE_BUTTON = (By.XPATH, "//a[text()='Профиль']")
    
    # Кнопка выхода - обновленные локаторы
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
    LOGOUT_BUTTON_ALT1 = (By.XPATH, "//button[contains(., 'Выход')]")
    LOGOUT_BUTTON_ALT2 = (By.XPATH, "//*[contains(text(), 'Выход') and (self::button or self::a)]")
    
    # Новые локаторы на основе диагностики
    LOGOUT_BUTTON_CLASS = (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and contains(text(), 'Выход')]")
    LOGOUT_BUTTON_CONTAINS = (By.XPATH, "//*[contains(@class, 'Account_button__14Yp3') and contains(text(), 'Выход')]")
    
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