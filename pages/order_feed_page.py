from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from selenium.webdriver.support.ui import WebDriverWait
import allure


class OrderFeedPage(BasePage):
    
    @allure.step("Получить количество заказов за все время")
    def get_total_orders_count(self):
        return int(self.get_text(OrderFeedPageLocators.TOTAL_ORDERS_COUNT))

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        return int(self.get_text(OrderFeedPageLocators.TODAY_ORDERS_COUNT))

    @allure.step("Получить заказы в работе")
    def get_orders_in_progress(self):
        orders = self.find_elements(OrderFeedPageLocators.ORDERS_IN_PROGRESS_LIST, timeout=10)
        return [order.text for order in orders]

    @allure.step("Проверить наличие заказа в работе")
    def is_order_in_progress(self, order_number):
        orders = self.get_orders_in_progress()
        return any(order_number in order for order in orders)

    @allure.step("Дождаться появления заказов в работе")
    def wait_for_orders_in_progress(self, timeout=30):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(
            lambda driver: len(self.find_elements(OrderFeedPageLocators.ORDERS_IN_PROGRESS_LIST)) > 0
        )