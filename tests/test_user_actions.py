import pytest
import allure
from pages.main_page import MainPage
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from services.auth_service import AuthService
from data.test_scenarios import TestScenarios


@allure.feature("User Actions")
class TestUserActions:

    @allure.title("Переход в личный кабинет для авторизованного пользователя")
    def test_navigate_to_personal_account_when_authenticated(self, driver, authenticated_user):
        account_page = AccountPage(driver)
        current_url = account_page.get_current_url()
        
        assert "account" in current_url or "profile" in current_url
        assert account_page.is_logout_button_visible()

    @allure.title("Переход на страницу логина для неавторизованного пользователя")
    def test_navigate_to_login_page_when_not_authenticated(self, driver, not_authenticated_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.click_personal_account()
        login_page.wait_for_page_loaded()
        
        assert login_page.is_current_page()

    @allure.title("Навигация через конструктор из личного кабинета")
    def test_navigation_via_constructor_from_account(self, driver, authenticated_user):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        account_page.click_constructor()
        main_page.wait_for_page_loaded()
        
        assert main_page.is_current_page()

    @allure.title("Выход из системы")
    def test_user_logout(self, driver, authenticated_user):
        account_page = AccountPage(driver)
        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        original_url = account_page.get_current_url()
        
        account_page.click_logout()
        login_page.wait_for_page_loaded()
        
        current_url = login_page.get_current_url()
        
        assert "account" not in current_url and "profile" not in current_url
        assert login_page.is_current_page()
        
        # Проверяем, что после выхода при попытке перейти в ЛК открывается логин
        main_page.open()
        main_page.click_personal_account()
        login_page.wait_for_page_loaded()
        
        assert login_page.is_current_page()