from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from data.urls import URLs
import allure


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, URLs.PROFILE_PAGE)

    @allure.step("Проверить что текущая страница - профиль")
    def is_current_page(self):
        current_url = self.get_current_url()
        return any(keyword in current_url for keyword in ["account", "profile", "user"])

    @allure.step("Кликнуть на кнопку выхода")
    def click_logout(self):
        self.wait_for_no_overlay()
        
        logout_locators = [
            AccountPageLocators.LOGOUT_BUTTON_CLASS, 
            AccountPageLocators.LOGOUT_BUTTON_CONTAINS,
            AccountPageLocators.LOGOUT_BUTTON,
            AccountPageLocators.LOGOUT_BUTTON_ALT1,
            AccountPageLocators.LOGOUT_BUTTON_ALT2
        ]
        
        for locator in logout_locators:
            try:
                if self.is_element_visible(locator, timeout=3):
                    original_url = self.get_current_url()
                    
                    try:
                        self.click(locator)
                    except Exception:
                        self.click_js(locator)
                    
                    self.wait_for_url_change(original_url, timeout=10)
                    return True
                    
            except Exception:
                continue
                    
        raise Exception("Не удалось найти и нажать кнопку выхода")

    @allure.step("Кликнуть на конструктор")
    def click_constructor(self):
        self.wait_for_no_overlay()
        self.click_js(AccountPageLocators.CONSTRUCTOR_LINK)
        self.wait_for_page_loaded()

    @allure.step("Кликнуть на логотип")
    def click_logo(self):
        self.wait_for_no_overlay()
        original_url = self.get_current_url()
        
        # Используем базовые методы вместо прямого обращения к driver
        if "firefox" in self.get_browser_name():
            self.click_js(AccountPageLocators.LOGO_LINK)
        else:
            self.click(AccountPageLocators.LOGO_LINK)
            
        self.wait_for_url_change(original_url)
        self.wait_for_page_loaded()

    @allure.step("Проверить наличие кнопки выхода")
    def is_logout_button_visible(self):
        for locator in [
            AccountPageLocators.LOGOUT_BUTTON_CLASS,
            AccountPageLocators.LOGOUT_BUTTON_CONTAINS,
            AccountPageLocators.LOGOUT_BUTTON,
            AccountPageLocators.LOGOUT_BUTTON_ALT1,
            AccountPageLocators.LOGOUT_BUTTON_ALT2
        ]:
            if self.is_element_visible(locator, timeout=2):
                return True
        return False