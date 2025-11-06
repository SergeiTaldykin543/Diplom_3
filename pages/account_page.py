from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from utilities.urls import URLs
import allure

class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, URLs.PROFILE_PAGE)

    @allure.step("Проверить что текущая страница - профиль")
    def is_current_page(self):
        current_url = self.get_current_url()
        return "account" in current_url or "profile" in current_url

    @allure.step("Кликнуть на кнопку выхода")
    def click_logout(self):
        self.wait_for_no_overlay()
        self.click_js(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step("Кликнуть на конструктор")
    def click_constructor(self):
        self.wait_for_no_overlay()
        self.click_js(AccountPageLocators.CONSTRUCTOR_LINK)
        self.wait_for_page_loaded()

    @allure.step("Кликнуть на логотип")
    def click_logo(self):
        self.wait_for_no_overlay()
        self.click_js(AccountPageLocators.LOGO_LINK)
        self.wait_for_page_loaded()