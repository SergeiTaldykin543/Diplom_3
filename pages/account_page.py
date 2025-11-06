from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from utilities.urls import URLs
import allure
from selenium.webdriver.common.action_chains import ActionChains

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
                    print(f"Найдена кнопка выхода по локатору: {locator}")
                    
                    original_url = self.get_current_url()
                    
                    try:
                        self.click(locator)
                    except:
                        self.click_js(locator)
                    
                    try:
                        self.wait_for_url_change(original_url, timeout=10)
                        print("URL изменился после выхода")
                        return True
                    except:
                        from pages.login_page import LoginPage
                        login_page = LoginPage(self.driver)
                        if login_page.is_current_page():
                            print("Перешли на страницу логина")
                            return True
                        else:
                            from pages.main_page import MainPage
                            main_page = MainPage(self.driver)
                            if main_page.is_current_page():
                                print("Перешли на главную страницу")
                                return True
                    
                    return True
                    
            except Exception as e:
                print(f"Ошибка с локатором {locator}: {e}")
                continue
                    
        raise Exception("Не удалось найти и нажать кнопку выхода")

    @allure.step("Выйти из системы через UI")
    def logout_via_ui(self):
        self.wait_for_no_overlay()
        
        try:
            logout_button = self.find_element(AccountPageLocators.LOGOUT_BUTTON_CLASS)
            
            original_url = self.get_current_url()
            
            approaches = [
                lambda: logout_button.click(), 
                lambda: self.driver.execute_script("arguments[0].click();", logout_button), 
                lambda: ActionChains(self.driver).move_to_element(logout_button).click().perform(),  
            ]
            
            for approach in approaches:
                try:
                    approach()
                    
                    self.wait_for_page_loaded(timeout=10)
                    
                    current_url = self.get_current_url()
                    if current_url != original_url:
                        print(f"Выход успешен! Перешли с {original_url} на {current_url}")
                        return True
                        
                except Exception as e:
                    print(f"Подход не сработал: {e}")
                    continue
        
        except Exception as e:
            print(f"Ошибка в альтернативном методе выхода: {e}")
        
        current_url = self.get_current_url()
        print(f"После попытки выхода остались на: {current_url}")
        return False

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