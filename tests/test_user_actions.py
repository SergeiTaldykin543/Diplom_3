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

    @allure.title("Навигация через конструктор из личного кабинета")
    def test_navigation_via_constructor_from_account(self, driver, authenticated_user):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        account_page.click_constructor()
        main_page.wait_for_page_loaded()
        
        assert main_page.is_current_page()

    @allure.title("Выход из системы перенаправляет с профиля")
    def test_logout_redirects_from_profile(self, driver, authenticated_user):
        account_page = AccountPage(driver)
        
        original_url = driver.current_url
        account_page.click_logout()
        
        current_url = driver.current_url
        assert current_url != original_url
        assert "account" not in current_url
        assert "profile" not in current_url

    @allure.title("После выхода открывается главная страница или логин")
    def test_after_logout_opens_main_or_login_page(self, driver, authenticated_user):
        account_page = AccountPage(driver)
        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        account_page.click_logout()
        main_page.wait_for_page_loaded()
        
        current_url = driver.current_url
        is_main_page = main_page.is_current_page()
        is_login_page = login_page.is_current_page()
        
        assert is_main_page or is_login_page

    @allure.title("После выхода требуется авторизация для доступа к личному кабинету")
    def test_requires_auth_after_logout(self, driver, authenticated_user):
        account_page = AccountPage(driver)
        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        account_page.click_logout()
        main_page.wait_for_page_loaded()
        
        # Пытаемся перейти в личный кабинет
        if main_page.is_current_page():
            main_page.click_personal_account()
            login_page.wait_for_page_loaded()
            assert login_page.is_current_page()