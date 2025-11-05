import pytest
import allure


class TestOrderFeed:
    """Тесты ленты заказов"""
    
    @allure.title("Увеличение счетчика заказов за все время")
    def test_total_orders_counter_increases(self, authenticated_user, order_feed_page):
        authenticated_user.click_order_feed()
        initial_total = order_feed_page.get_total_orders_count()
        
        authenticated_user.click_constructor()
        authenticated_user.add_ingredient_to_constructor(0)
        authenticated_user.place_order()
        authenticated_user.close_modal()
        
        authenticated_user.click_order_feed()
        new_total = order_feed_page.get_total_orders_count()
        
        assert new_total > initial_total

    @allure.title("Увеличение счетчика заказов за сегодня")
    def test_today_orders_counter_increases(self, authenticated_user, order_feed_page):
        authenticated_user.click_order_feed()
        initial_today = order_feed_page.get_today_orders_count()
        
        authenticated_user.click_constructor()
        authenticated_user.add_ingredient_to_constructor(0)
        authenticated_user.place_order()
        authenticated_user.close_modal()
        
        authenticated_user.click_order_feed()
        new_today = order_feed_page.get_today_orders_count()
        
        assert new_today > initial_today

    @allure.title("Появление заказа в разделе 'В работе'")
    @pytest.mark.xfail(reason="Баг: номер в 'В работе' может не совпадать с номером из модального окна")
    def test_order_appears_in_progress(self, authenticated_user, order_feed_page):
        authenticated_user.add_ingredient_to_constructor(0)
        authenticated_user.place_order()
        order_number = authenticated_user.get_order_number()
        authenticated_user.close_modal()
        
        authenticated_user.click_order_feed()
        order_feed_page.wait_for_orders_in_progress()
        
        assert order_feed_page.is_order_in_progress(order_number)