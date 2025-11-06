import pytest
import allure
from data.working_data import WorkingData
from utilities.urls import URLs
import time

@allure.feature("Navigation")
class TestNavigation:
    
    @allure.title("Test navigation to Constructor")
    @allure.description("Test navigating from order feed to constructor")
    def test_navigate_to_constructor(self, driver, login):
        from pages.main_page import MainPage
        
        main_page = MainPage(driver)
        
        with allure.step("Click on Order Feed"):
            main_page.click_order_feed()
            time.sleep(2)
        
        with allure.step("Verify we are on order feed page"):
            assert URLs.ORDER_FEED_PAGE in driver.current_url
        
        with allure.step("Click on Constructor"):
            main_page.click_constructor()
            time.sleep(2)
        
        with allure.step("Verify we are on main page"):
            assert URLs.MAIN_PAGE in driver.current_url
    
    @allure.title("Test navigation to Order Feed")
    @allure.description("Test navigating from main page to order feed")
    def test_navigate_to_order_feed(self, driver, login):
        from pages.main_page import MainPage
        
        main_page = MainPage(driver)
        
        with allure.step("Click on Order Feed"):
            main_page.click_order_feed()
            time.sleep(2)
        
        with allure.step("Verify we are on order feed page"):
            assert URLs.ORDER_FEED_PAGE in driver.current_url
    
    @allure.title("Test navigation to Personal Account")
    @allure.description("Test navigating to personal account")
    def test_navigate_to_personal_account(self, driver, login):
        from pages.main_page import MainPage
        
        main_page = MainPage(driver)
        
        with allure.step("Click on Personal Account"):
            main_page.click_personal_account()
            time.sleep(3)
        
        with allure.step("Verify we are on account page"):
            current_url = driver.current_url
            # После успешного логина должно перекинуть на страницу профиля
            assert "account" in current_url or "profile" in current_url, f"Expected account page, got: {current_url}"
            print(f"✅ Successfully navigated to account: {current_url}")