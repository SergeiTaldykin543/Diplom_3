import pytest
import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from data.test_scenarios import TestScenarios

@allure.feature("Order Feed")
class TestOrderFeed:

    @allure.title("Переход на страницу ленты заказов")
    def test_navigate_to_order_feed_page(self, driver, authenticated_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.click_order_feed()
        order_feed_page.wait_for_order_feed_loaded()
        
        assert order_feed_page.is_current_page()

    @allure.title("Отображение счетчиков заказов")
    def test_order_counters_are_displayed(self, driver, authenticated_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.click_order_feed()
        order_feed_page.wait_for_order_feed_loaded()
        
        all_time = order_feed_page.get_orders_done_all_time()
        today = order_feed_page.get_orders_done_today()
        
        assert all_time >= 0
        assert today >= 0

    @allure.title("Доступность ленты заказов")
    def test_order_feed_accessible(self, driver, authenticated_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.click_order_feed()
        order_feed_page.wait_for_order_feed_loaded()
        
        order_items = order_feed_page.get_order_items()
        assert order_items is not None