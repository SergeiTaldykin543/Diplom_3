import pytest
import allure
from data.urls import Urls


class TestNavigation:
    """Тесты навигации по приложению"""
    
    @allure.title("Переход в конструктор из ленты заказов")
    def test_navigate_to_constructor_from_feed(self, authenticated_user):
        authenticated_user.click_order_feed()
        assert Urls.FEED_URL in authenticated_user.get_current_url()
        
        authenticated_user.click_constructor()
        assert Urls.BASE_URL in authenticated_user.get_current_url()

    @allure.title("Переход в ленту заказов из конструктора")
    def test_navigate_to_feed_from_constructor(self, authenticated_user):
        authenticated_user.click_order_feed()
        assert Urls.FEED_URL in authenticated_user.get_current_url()

    @allure.title("Переход в личный кабинет")
    def test_navigate_to_account(self, authenticated_user):
        authenticated_user.click_account()
        assert Urls.ACCOUNT_URL in authenticated_user.get_current_url()