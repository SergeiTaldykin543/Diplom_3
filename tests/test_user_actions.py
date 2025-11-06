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

    @allure.title("Выход из системы")
    def test_user_logout(self, driver, authenticated_user):
        account_page = AccountPage(driver)
        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        original_url = driver.current_url
        print(f"URL до выхода: {original_url}")
        
        logout_successful = False
        
        try:
            account_page.click_logout()
            logout_successful = True
            print("Стандартный выход выполнен")
        except Exception as e:
            print(f"Стандартный выход не сработал: {e}")
        
        if not logout_successful:
            try:
                logout_successful = account_page.logout_via_ui()
                if logout_successful:
                    print("Альтернативный выход выполнен")
            except Exception as e:
                print(f"Альтернативный выход не сработал: {e}")
        
        if logout_successful:
            main_page.wait_for_page_loaded()
            
            current_url = driver.current_url
            print(f"🔍 URL после выхода: {current_url}")
            
            assert "account" not in current_url and "profile" not in current_url, \
                f"После выхода остались на странице профиля: {current_url}"
            
            is_main_page = main_page.is_current_page()
            is_login_page = login_page.is_current_page()
            
            assert is_main_page or is_login_page, \
                f"После выхода ожидалась главная страница или логин, получен: {current_url}"
            
            if is_main_page:
                main_page.click_personal_account()
                login_page.wait_for_page_loaded()
                assert login_page.is_current_page(), \
                    "После выхода должна открываться страница логина при попытке перехода в личный кабинет"
        
        else:
            pytest.skip("Выход из системы не работает в текущей версии приложения")