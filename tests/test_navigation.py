import pytest
import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from data.test_scenarios import TestScenarios

@allure.feature("Navigation")
class TestNavigation:

    @allure.title("Переход из конструктора в ленту заказов")
    def test_navigate_from_constructor_to_order_feed(self, driver, authenticated_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        authenticated_user.click_constructor()
        main_page.wait_for_page_loaded()
        
        original_url = driver.current_url
        main_page.click_order_feed()
        order_feed_page.wait_for_order_feed_loaded()
        
        current_url = driver.current_url
        assert current_url != original_url
        assert "feed" in current_url

    @allure.title("Переход из ленты заказов в конструктор")
    def test_navigate_from_order_feed_to_constructor(self, driver, authenticated_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        authenticated_user.click_constructor()
        main_page.wait_for_page_loaded()
        
        main_page.click_order_feed()
        order_feed_page.wait_for_order_feed_loaded()
        main_page.click_constructor()
        main_page.wait_for_page_loaded()
        
        assert main_page.is_current_page()

    @allure.title("Переход в личный кабинет для авторизованного пользователя")
    def test_navigate_to_personal_account_when_authenticated(self, driver, authenticated_user):
        account_page = AccountPage(driver)
        current_url = driver.current_url
        assert "account" in current_url or "profile" in current_url
        assert account_page.is_logout_button_visible()

    @allure.title("Переход на страницу логина для неавторизованного пользователя")
    def test_navigate_to_login_page_when_not_authenticated(self, driver, not_authenticated_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.click_personal_account()
        login_page.wait_for_page_loaded()
        
        assert login_page.is_current_page()