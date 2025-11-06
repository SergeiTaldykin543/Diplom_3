import pytest
import allure
from utilities.urls import URLs
import time

@allure.feature("User Actions")
class TestUserActions:
    
    @allure.title("Test user logout")
    @allure.description("Test that user can logout successfully")
    def test_user_logout(self, driver, login):
        from pages.account_page import AccountPage
        from pages.main_page import MainPage
        
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        
        with allure.step("Navigate to profile page"):
            main_page.click_personal_account()
            time.sleep(3)
        
        with allure.step("Verify we are on account page"):
            current_url = driver.current_url
            assert "account" in current_url or "profile" in current_url, f"Expected account page, got: {current_url}"
        
        with allure.step("Click logout button"):
            account_page.click_logout()
            time.sleep(3)
        
        with allure.step("Verify redirected to login page"):
            assert URLs.LOGIN_PAGE in driver.current_url
            print("✅ Logout successful!")
    
    @allure.title("Test navigation via logo")
    @allure.description("Test that clicking logo navigates to main page")
    def test_navigation_via_logo(self, driver, login):
        from pages.account_page import AccountPage
        from pages.main_page import MainPage
        
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        
        with allure.step("Navigate to profile page"):
            main_page.click_personal_account()
            time.sleep(3)
        
        with allure.step("Click on logo"):
            account_page.click_logo()
            time.sleep(2)
        
        with allure.step("Verify we are on main page"):
            assert URLs.MAIN_PAGE in driver.current_url
    
    @allure.title("Test navigation via constructor from profile")
    @allure.description("Test that clicking constructor navigates to main page from profile")
    def test_navigation_via_constructor(self, driver, login):
        from pages.account_page import AccountPage
        from pages.main_page import MainPage
        
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        
        with allure.step("Navigate to profile page"):
            main_page.click_personal_account()
            time.sleep(3)
        
        with allure.step("Click on constructor"):
            account_page.click_constructor()
            time.sleep(2)
        
        with allure.step("Verify we are on main page"):
            assert URLs.MAIN_PAGE in driver.current_url