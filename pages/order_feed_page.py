from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
import allure
import time

class OrderFeedPage(BasePage):
    
    @allure.step("Получить количество выполненных заказов за все время")
    def get_orders_done_all_time(self):
        try:
            text = self.get_text(OrderFeedLocators.ORDERS_DONE_ALL_TIME)
            return int(text) if text and text.isdigit() else 0
        except Exception as e:
            allure.attach(f"Error getting all time orders: {str(e)}", "Error")
            return 0
    
    @allure.step("Получить количество выполненных заказов за сегодня")
    def get_orders_done_today(self):
        try:
            text = self.get_text(OrderFeedLocators.ORDERS_DONE_TODAY)
            return int(text) if text and text.isdigit() else 0
        except Exception as e:
            allure.attach(f"Error getting today orders: {str(e)}", "Error")
            return 0
    
    @allure.step("Получить заказы в работе")
    def get_orders_in_progress(self):
        try:
            # Даем время для загрузки заказов
            time.sleep(2)
            elements = self.find_elements(OrderFeedLocators.ORDERS_IN_PROGRESS)
            return [elem.text for elem in elements if elem.text]
        except Exception as e:
            allure.attach(f"Error getting orders in progress: {str(e)}", "Error")
            return []
    
    @allure.step("Кликнуть на заказ по индексу {index}")
    def click_order(self, index=0):
        try:
            orders = self.find_elements(OrderFeedLocators.ORDER_ITEMS)
            if orders and index < len(orders):
                orders[index].click()
                time.sleep(1)  # Ждем открытия модального окна
        except Exception as e:
            allure.attach(f"Error clicking order: {str(e)}", "Error")
    
    @allure.step("Получить номер последнего заказа")
    def get_latest_order_number(self):
        try:
            orders = self.find_elements(OrderFeedLocators.ORDER_ITEMS)
            if orders:
                order_number_element = orders[0].find_element(*OrderFeedLocators.ORDER_NUMBER)
                return order_number_element.text.strip() if order_number_element.text else None
        except Exception as e:
            allure.attach(f"Error getting latest order number: {str(e)}", "Error")
        return None
    
    @allure.step("Проверить видимость модального окна деталей заказа")
    def is_order_details_modal_visible(self):
        return self.is_element_visible(OrderFeedLocators.ORDER_DETAILS_MODAL)
    
    @allure.step("Получить номер заказа из модального окна")
    def get_order_details_number(self):
        try:
            return self.get_text(OrderFeedLocators.ORDER_DETAILS_NUMBER)
        except Exception as e:
            allure.attach(f"Error getting order details number: {str(e)}", "Error")
            return None
    
    @allure.step("Закрыть модальное окно деталей заказа")
    def close_order_details_modal(self):
        try:
            self.click(OrderFeedLocators.MODAL_CLOSE_BUTTON)
            time.sleep(1)
        except Exception as e:
            allure.attach(f"Error closing modal: {str(e)}", "Error")