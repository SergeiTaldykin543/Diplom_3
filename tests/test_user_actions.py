import pytest
import allure
from pages.main_page import MainPage
from pages.account_page import AccountPage


@allure.feature("User Actions")
class TestUserActions:
    
    @allure.title("Переход в личный кабинет")
    def test_navigate_to_personal_account(self, driver, login):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        
        main_page.click_personal_account()
        
        # Проверяем что перешли на страницу связанную с аккаунтом
        current_url = account_page.get_current_url()
        assert "account" in current_url or "profile" in current_url
    
    @allure.title("Навигация через конструктор")
    def test_navigation_via_constructor(self, driver, login):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        
        # Переходим в аккаунт
        main_page.click_personal_account()
        
        # Возвращаемся через конструктор
        account_page.click_constructor()
        
        assert main_page.is_current_page()