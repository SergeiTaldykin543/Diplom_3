from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from utilities.urls import URLs
import allure
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, URLs.MAIN_PAGE)

    @allure.step("Проверить что текущая страница - главная")
    def is_current_page(self):
        current_url = self.get_current_url()
        return self.url in current_url or "stellarburgers" in current_url

    @allure.step("Кликнуть на конструктор")
    def click_constructor(self):
        self.wait_for_no_overlay()
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait_for_page_loaded()

    @allure.step("Кликнуть на ленту заказов")
    def click_order_feed(self):
        self.wait_for_no_overlay()
        original_url = self.get_current_url()
        
        # Для Firefox используем JS клик чтобы обойти перекрытие
        if "firefox" in self.driver.name.lower():
            self.click_js(MainPageLocators.ORDER_FEED_BUTTON)
        else:
            self.click(MainPageLocators.ORDER_FEED_BUTTON)
            
        # Ждем навигации
        self.wait_for_url_change(original_url)
        self.wait_for_page_loaded()

    @allure.step("Кликнуть на личный кабинет")
    def click_personal_account(self):
        self.wait_for_no_overlay()
        original_url = self.get_current_url()
        
        # Для Firefox используем JS клик чтобы обойти перекрытие
        if "firefox" in self.driver.name.lower():
            self.click_js(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        else:
            self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
            
        # Ждем навигации
        self.wait_for_url_change(original_url)
        self.wait_for_page_loaded()

    @allure.step("Кликнуть на ингредиент по индексу {index}")
    def click_ingredient(self, index=0):
        try:
            self.wait_for_no_overlay()
            ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
            if ingredients and index < len(ingredients):
                ingredients[index].click()
                # Ждем появления модального окна
                self.wait_for_element_to_be_visible(MainPageLocators.INGREDIENT_MODAL)
                return True
            return False
        except:
            return False

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        try:
            self.click(MainPageLocators.MODAL_CLOSE_BUTTON)
            self.wait_for_element_to_disappear(MainPageLocators.INGREDIENT_MODAL)
            return True
        except:
            return False

    @allure.step("Проверить видимость модального окна")
    def is_modal_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL)

    @allure.step("Получить название ингредиента в модальном окне")
    def get_modal_ingredient_name(self):
        try:
            return self.get_text(MainPageLocators.MODAL_INGREDIENT_NAME)
        except:
            return ""

    @allure.step("Закрыть все модальные окна если есть")
    def close_all_modals_if_present(self):
        """Закрывает все модальные окна если они присутствуют"""
        try:
            # Ищем кнопки закрытия модальных окон
            close_buttons = self.driver.find_elements(By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
            for button in close_buttons:
                try:
                    button.click()
                except:
                    pass
            # Ждем исчезновения модальных окон
            self.wait_for_no_overlay()
            return True
        except:
            return False