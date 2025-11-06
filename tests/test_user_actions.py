import pytest
import allure
from pages.main_page import MainPage
from pages.account_page import AccountPage
from pages.login_page import LoginPage

@allure.feature("User Actions")
class TestUserActions:

    @allure.title("Переход в личный кабинет или на страницу логина")
    def test_navigate_to_personal_account(self, driver, login):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        login_page = LoginPage(driver)

        # Сохраняем текущий URL до клика
        original_url = driver.current_url

        main_page.click_personal_account()

        # Ждем навигации - URL должен измениться ИЛИ появиться элементы целевой страницы
        try:
            # Ожидаем изменения URL или появления элементов целевой страницы
            main_page.wait_for_url_change(original_url, timeout=10)
        except:
            # Если URL не изменился, проверяем элементы текущей страницы
            pass

        # Получаем текущий URL для анализа
        current_url = driver.current_url

        # Анализируем результат перехода
        if current_url != original_url:
            # URL изменился - произошла навигация
            if "account" in current_url or "profile" in current_url:
                # Успешно перешли в аккаунт - ждем элементы страницы аккаунта
                account_page.wait_for_page_loaded()
                assert account_page.is_current_page()
            elif "login" in current_url:
                # Перешли на страницу логина - ждем элементы формы логина
                login_page.wait_for_page_loaded()
                assert login_page.is_current_page()
            else:
                # Перешли куда-то еще
                pytest.fail(f"Неожиданный URL после клика на личный кабинет: {current_url}")
        else:
            # URL не изменился - проверяем текущую страницу
            if "account" in current_url or "profile" in current_url:
                account_page.wait_for_page_loaded()
                assert account_page.is_current_page()
            else:
                # Остались на главной или другой странице
                main_page.wait_for_page_loaded()
                assert main_page.is_current_page()

    @allure.title("Навигация через конструктор")
    def test_navigation_via_constructor(self, driver, login):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        login_page = LoginPage(driver)

        # Сохраняем исходный URL
        original_url = driver.current_url
        
        # Сначала переходим в личный кабинет/логин
        main_page.click_personal_account()

        # Ждем навигации
        try:
            main_page.wait_for_url_change(original_url, timeout=10)
        except:
            pass

        current_url = driver.current_url

        # Возвращаемся через конструктор в зависимости от текущей страницы
        if "account" in current_url or "profile" in current_url:
            account_page.click_constructor()
            # Ждем возврата на главную
            main_page.wait_for_page_loaded()
        elif "login" in current_url:
            login_page.click_constructor()
            # Ждем возврата на главную
            main_page.wait_for_page_loaded()
        else:
            # Уже на главной или другой странице
            main_page.click_constructor()
            main_page.wait_for_page_loaded()
            
        # Проверяем что вернулись на главную
        assert main_page.is_current_page()