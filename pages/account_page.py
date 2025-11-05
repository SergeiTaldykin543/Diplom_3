from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
import allure


class AccountPage(BasePage):
    
    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.click(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step("Проверить открытие страницы профиля")
    def is_profile_page_opened(self):
        return self.is_element_visible(AccountPageLocators.PROFILE_LINK)