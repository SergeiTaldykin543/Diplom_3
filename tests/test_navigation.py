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

        original_url = driver.current_url
        main_page.click_order_feed()
        
        # Ждем загрузки ленты заказов
        order_feed_page.wait_for_order_feed_loaded()
        
        # Проверяем что URL изменился
        current_url = driver.current_url
        assert current_url != original_url, "URL не изменился после перехода"
        assert "feed" in current_url or "order-feed" in current_url, f"Ожидался URL ленты заказов, получен: {current_url}"

    @allure.title("Переход из ленты заказов в конструктор")
    def test_navigate_from_order_feed_to_constructor(self, driver, login):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        # Переходим в ленту заказов
        original_url = driver.current_url
        main_page.click_order_feed()
        order_feed_page.wait_for_order_feed_loaded()
        
        # Возвращаемся в конструктор
        main_page.click_constructor()
        main_page.wait_for_page_loaded()
        
        # Проверяем что вернулись на главную
        assert main_page.is_current_page()

    @allure.title("Переход в личный кабинет")
    def test_navigate_to_personal_account(self, driver, login):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        original_url = driver.current_url
        main_page.click_personal_account()
        
        # Ждем навигации
        main_page.wait_for_url_change(original_url)
        
        # Проверяем URL после перехода
        current_url = driver.current_url
        
        if "account" in current_url or "profile" in current_url:
            account_page.wait_for_page_loaded()
            assert account_page.is_current_page()
        elif "login" in current_url:
            from pages.login_page import LoginPage
            login_page = LoginPage(driver)
            login_page.wait_for_page_loaded()
            assert login_page.is_current_page()
        else:
            main_page.wait_for_page_loaded()
            assert main_page.is_current_page()