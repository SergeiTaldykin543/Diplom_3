from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data.urls import URLs
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, URLs.MAIN_PAGE)

    @allure.step("Проверить что текущая страница - главная")
    def is_current_page(self):
        current_url = self.get_current_url()
        return (URLs.MAIN_PAGE in current_url or "stellarburgers" in current_url) and \
               "account" not in current_url and "profile" not in current_url

    @allure.step("Кликнуть на конструктор")
    def click_constructor(self):
        self.wait_for_no_overlay()
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait_for_page_loaded()

    @allure.step("Кликнуть на ленту заказов")
    def click_order_feed(self):
        self.wait_for_no_overlay()
        original_url = self.get_current_url()
        
        if "firefox" in self.get_browser_name():
            self.click_js(MainPageLocators.ORDER_FEED_BUTTON)
        else:
            self.click(MainPageLocators.ORDER_FEED_BUTTON)
            
        self.wait_for_url_change(original_url)
        self.wait_for_page_loaded()

    @allure.step("Кликнуть на личный кабинет")
    def click_personal_account(self):
        self.wait_for_no_overlay()
        original_url = self.get_current_url()
        
        if "firefox" in self.get_browser_name():
            self.click_js(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        else:
            self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
            
        self.wait_for_url_change(original_url)
        self.wait_for_page_loaded()

    @allure.step("Кликнуть на ингредиент по индексу")
    def click_ingredient(self, index=0):
        try:
            self.wait_for_no_overlay()
            ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
            if ingredients and index < len(ingredients):
                ingredients[index].click()
                self.wait_for_element_to_be_visible(MainPageLocators.INGREDIENT_MODAL)
                return True
            return False
        except Exception:
            return False

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        try:
            self.click(MainPageLocators.MODAL_CLOSE_BUTTON)
            self.wait_for_element_to_disappear(MainPageLocators.INGREDIENT_MODAL)
            return True
        except Exception:
            return False

    @allure.step("Проверить видимость модального окна")
    def is_modal_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL)

    @allure.step("Получить название ингредиента в модальном окне")
    def get_modal_ingredient_name(self):
        try:
            return self.get_text(MainPageLocators.MODAL_INGREDIENT_NAME)
        except Exception:
            return ""