from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from data.test_data import TestData
import allure

class LoginPage(BasePage):

    @allure.step("Ввести email: {email}")
    def enter_email(self, email):
        print(f"Entering email: {email}")
        self.send_keys(AccountPageLocators.EMAIL_INPUT, email)
        # Проверяем, что email ввелся
        entered_email = self.find_element(AccountPageLocators.EMAIL_INPUT).get_attribute('value')
        print(f"Email field contains: {entered_email}")

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        print(f"Entering password: {'*' * len(password)}")
        self.send_keys(AccountPageLocators.PASSWORD_INPUT, password)
        # Проверяем, что пароль ввелся
        entered_password = self.find_element(AccountPageLocators.PASSWORD_INPUT).get_attribute('value')
        print(f"Password field contains: {'*' * len(entered_password)}")

    @allure.step("Кликнуть на кнопку входа")
    def click_login_button(self):
        print("Clicking login button")
        button = self.find_element(AccountPageLocators.LOGIN_BUTTON)
        print(f"Login button text: {button.text}")
        print(f"Login button enabled: {button.is_enabled()}")
        button.click()

    @allure.step("Выполнить вход")
    def login(self, email=TestData.EMAIL, password=TestData.PASSWORD):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    @allure.step("Проверить видимость формы входа")
    def is_login_form_visible(self):
        return self.is_element_visible(AccountPageLocators.LOGIN_BUTTON)

    @allure.step("Получить текст ошибки")
    def get_error_message(self):
        try:
            return self.get_text(AccountPageLocators.ERROR_MESSAGE)
        except:
            return "No error message found"