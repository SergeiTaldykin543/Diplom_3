from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
import allure

class AccountPage(BasePage):
    
    @allure.step("Кликнуть на кнопку выхода")
    def click_logout(self):
        self.click(AccountPageLocators.LOGOUT_BUTTON)
    
    @allure.step("Кликнуть на конструктор")
    def click_constructor(self):
        self.click(AccountPageLocators.CONSTRUCTOR_LINK)
    
    @allure.step("Кликнуть на логотип")
    def click_logo(self):
        self.click(AccountPageLocators.LOGO_LINK)
    
    @allure.step("Проверить видимость кнопки выхода")
    def is_logout_button_visible(self):
        return self.is_element_visible(AccountPageLocators.LOGOUT_BUTTON)