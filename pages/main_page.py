from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure

class MainPage(BasePage):
    
    @allure.step("Кликнуть на конструктор")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)
    
    @allure.step("Кликнуть на ленту заказов")
    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)
    
    @allure.step("Кликнуть на личный кабинет")
    def click_personal_account(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    
    @allure.step("Кликнуть на ингредиент по индексу {index}")
    def click_ingredient(self, index=0):
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        if ingredients:
            ingredients[index].click()
    
    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        try:
            # Ждем пока модальное окно станет видимым
            self.find_element(MainPageLocators.MODAL_CLOSE_BUTTON)
            self.click(MainPageLocators.MODAL_CLOSE_BUTTON)
            # Ждем пока модальное окно закроется
            self.wait_for_element_to_disappear(MainPageLocators.INGREDIENT_MODAL)
        except Exception as e:
            allure.attach(f"Error closing modal: {str(e)}", "Error")
    
    @allure.step("Проверить видимость модального окна")
    def is_modal_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL)
    
    @allure.step("Получить название ингредиента в модальном окне")
    def get_modal_ingredient_name(self):
        return self.get_text(MainPageLocators.MODAL_INGREDIENT_NAME)
    
    @allure.step("Получить счетчик ингредиента по индексу {index}")
    def get_ingredient_counter(self, index=0):
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        if ingredients and index < len(ingredients):
            counters = ingredients[index].find_elements(*MainPageLocators.INGREDIENT_COUNTER)
            if counters:
                counter_text = counters[0].text
                return int(counter_text) if counter_text.isdigit() else 0
        return 0
    
    @allure.step("Получить номер заказа из модального окна")
    def get_order_number(self):
        return self.get_text(MainPageLocators.ORDER_NUMBER)
    
    @allure.step("Кликнуть на кнопку оформления заказа")
    def click_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON)
    
    @allure.step("Получить общую стоимость заказа")
    def get_order_total(self):
        return self.get_text(MainPageLocators.ORDER_TOTAL)