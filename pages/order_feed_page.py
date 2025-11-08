from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from data.urls import URLs
import allure


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, URLs.ORDER_FEED_PAGE)

    @allure.step("Проверить что текущая страница - лента заказов")
    def is_current_page(self):
        current_url = self.get_current_url()
        return "feed" in current_url

    @allure.step("Подождать загрузки ленты заказов")
    def wait_for_order_feed_loaded(self, timeout=15):
        try:
            self.wait_for_element_to_be_visible(OrderFeedLocators.ORDER_ITEMS, timeout=timeout)
            return True
        except Exception:
            try:
                self.wait_for_element_to_be_visible(OrderFeedLocators.ORDERS_DONE_ALL_TIME, timeout=5)
                return True
            except Exception:
                try:
                    self.wait_for_element_to_be_visible(OrderFeedLocators.ORDERS_DONE_TODAY, timeout=5)
                    return True
                except Exception:
                    return False

    @allure.step("Получить количество выполненных заказов за все время")
    def get_orders_done_all_time(self):
        try:
            if self.is_element_visible(OrderFeedLocators.ORDERS_DONE_ALL_TIME):
                text = self.get_text(OrderFeedLocators.ORDERS_DONE_ALL_TIME)
                return int(text) if text and text.isdigit() else 0
            return 0
        except Exception:
            return 0

    @allure.step("Получить количество выполненных заказов за сегодня")
    def get_orders_done_today(self):
        try:
            if self.is_element_visible(OrderFeedLocators.ORDERS_DONE_TODAY):
                text = self.get_text(OrderFeedLocators.ORDERS_DONE_TODAY)
                return int(text) if text and text.isdigit() else 0
            return 0
        except Exception:
            return 0

    @allure.step("Получить список заказов")
    def get_order_items(self):
        try:
            return self.find_elements(OrderFeedLocators.ORDER_ITEMS)
        except Exception:
            return []