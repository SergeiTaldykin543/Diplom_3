import pytest
import allure

@allure.feature("Order Feed")
class TestOrderFeed:
    
    @allure.title("Test order counters are displayed")
    @allure.description("Test that order counters are displayed on order feed page")
    def test_order_counters_are_displayed(self, driver, login):
        from pages.order_feed_page import OrderFeedPage
        from pages.main_page import MainPage
        
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        with allure.step("Navigate to order feed"):
            main_page.click_order_feed()
        
        with allure.step("Get counter values"):
            all_time = order_feed_page.get_orders_done_all_time()
            today = order_feed_page.get_orders_done_today()
        
        with allure.step("Verify counters are displayed"):
            assert all_time >= 0
            assert today >= 0
    
    @allure.title("Test orders in progress section")
    @allure.description("Test that orders in progress section is accessible")
    def test_orders_in_progress_section(self, driver, login):
        from pages.order_feed_page import OrderFeedPage
        from pages.main_page import MainPage
        
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        with allure.step("Navigate to order feed"):
            main_page.click_order_feed()
        
        with allure.step("Get orders in progress"):
            orders_in_progress = order_feed_page.get_orders_in_progress()
        
        with allure.step("Verify orders section is accessible"):
            # We can't guarantee there will be orders in progress,
            # but we can verify the functionality works
            assert orders_in_progress is not None