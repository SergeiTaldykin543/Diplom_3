import pytest
import allure
from data.urls import Urls
from data.test_data import TestData


class TestAuthentication:
    """Тесты аутентификации"""
    
    @allure.title("Успешная авторизация пользователя")
    def test_successful_login(self, main_page):
        main_page.open(Urls.BASE_URL)
        main_page.login_via_account(TestData.EMAIL, TestData.PASSWORD)
        assert main_page.is_user_logged_in()

    @allure.title("Авторизация через главную страницу")
    def test_login_from_main_page(self, main_page):
        main_page.open(Urls.BASE_URL)
        main_page.login_from_main_page(TestData.EMAIL, TestData.PASSWORD)
        assert main_page.is_user_logged_in()

    @allure.title("Выход из аккаунта")
    def test_logout(self, authenticated_user):
        from pages.account_page import AccountPage
        
        authenticated_user.click_account()
        account_page = AccountPage(authenticated_user.driver)
        account_page.logout()
        
        assert not authenticated_user.is_user_logged_in()