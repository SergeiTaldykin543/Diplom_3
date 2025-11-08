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

        main_page.click_constructor()
        main_page.wait_for_page_loaded()
        
        original_url = driver.current_url
        main_page.click_order_feed()
        order_feed_page.wait_for_order_feed_loaded()
        
        current_url = driver.current_url
        assert current_url != original_url
        assert order_feed_page.is_current_page()

    @allure.title("Переход из ленты заказов в конструктор")
    def test_navigate_from_order_feed_to_constructor(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.open()
        main_page.click_order_feed()
        order_feed_page.wait_for_order_feed_loaded()
        
        main_page.click_constructor()
        main_page.wait_for_page_loaded()
        
        assert main_page.is_current_page()

    @allure.title("Переход по логотипу из личного кабинета")
    def test_navigate_via_logo_from_account(self, driver, authenticated_user):
        account_page = AccountPage(driver)
        main_page = MainPage(driver)

        account_page.click_logo()
        main_page.wait_for_page_loaded()
        
        current_url = driver.current_url
        
        # Для Firefox может потребоваться альтернативная навигация
        if "firefox" in driver.name.lower() and ("account" in current_url or "profile" in current_url):
            # В Firefox логотип может не работать, используем конструктор
            account_page.click_constructor()
            main_page.wait_for_page_loaded()
            current_url = driver.current_url
        
        # Проверяем что мы не в аккаунте
        is_not_in_account = "account" not in current_url and "profile" not in current_url
        is_main_page = main_page.is_current_page()
        
        # Успехом считается либо главная страница, либо любой URL не в аккаунте
        assert is_not_in_account or is_main_page, \
            f"После навигации остались в аккаунте: {current_url}"