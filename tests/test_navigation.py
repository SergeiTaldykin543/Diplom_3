import pytest
import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.account_page import AccountPage


@allure.feature("Navigation")
class TestNavigation:
    
    @allure.title("Переход из конструктора в ленту заказов")
    def test_navigate_from_constructor_to_order_feed(self, driver, login):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        main_page.click_order_feed()
        
        assert order_feed_page.is_current_page()
    
    @allure.title("Переход из ленты заказов в конструктор")
    def test_navigate_from_order_feed_to_constructor(self, driver, login):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        main_page.click_order_feed()
        main_page.click_constructor()
        
        assert main_page.is_current_page()
    
    @allure.title("Переход в личный кабинет")
    def test_navigate_to_personal_account(self, driver, login):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        
        main_page.click_personal_account()
        
        # Проверяем что перешли на страницу аккаунта или логина
        current_url = account_page.get_current_url()
        assert "account" in current_url or "login" in current_url