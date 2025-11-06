from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from utilities.urls import URLs
import allure

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, URLs.LOGIN_PAGE)

    @allure.step("Проверить что текущая страница - логин")
    def is_current_page(self):
        return self.url in self.get_current_url()

    @allure.step("Ввести email: {email}")
    def enter_email(self, email):
        self.send_keys(AccountPageLocators.EMAIL_INPUT, email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.send_keys(AccountPageLocators.PASSWORD_INPUT, password)

    @allure.step("Кликнуть на кнопку входа")
    def click_login_button(self):
        self.wait_for_no_overlay()
        
        if "firefox" in self.driver.name.lower():
            self.click_js(AccountPageLocators.LOGIN_BUTTON)
        else:
            self.click(AccountPageLocators.LOGIN_BUTTON)

    @allure.step("Выполнить вход с email: {email}")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        self.wait_for_page_loaded()

    @allure.step("Кликнуть на конструктор со страницы логина")
    def click_constructor(self):
        self.wait_for_no_overlay()
        self.click_js(AccountPageLocators.CONSTRUCTOR_LINK)
        self.wait_for_page_loaded()