from selenium.webdriver.common.by import By


class AccountPageLocators:
    PROFILE_LINK = (By.XPATH, "//a[contains(text(), 'Профиль')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")