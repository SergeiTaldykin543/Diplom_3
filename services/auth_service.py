import allure
import time
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.account_page import AccountPage

class AuthService:

    @staticmethod
    @allure.step("Авторизовать пользователя")
    def login(driver, email, password):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        # Открываем страницу логина
        login_page.open()
        
        # Ждем загрузки формы логина
        login_page.wait_for_page_loaded()
        
        # Выполняем вход
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login_button()
        
        # Даем время для обработки логина (ожидание вместо sleep)
        main_page.wait_for_page_loaded(timeout=15)
        
        # В Firefox может потребоваться дополнительное ожидание
        if "firefox" in driver.name.lower():
            time.sleep(2)  # Краткая пауза только для Firefox
        
        return main_page

    @staticmethod
    @allure.step("Проверить авторизацию пользователя")
    def is_user_logged_in(driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        try:
            # Сохраняем текущий URL
            original_url = driver.current_url
            
            # Ждем исчезновения возможных оверлеев
            main_page.wait_for_no_overlay()
            
            # Пробуем перейти в личный кабинет
            main_page.click_personal_account()
            
            # Ждем навигации
            main_page.wait_for_url_change(original_url, timeout=5)
            
            current_url = driver.current_url
            
            # Если перешли на страницу логина - не авторизованы
            if "login" in current_url:
                # Возвращаемся на исходную страницу
                driver.get(original_url)
                return False
            else:
                # Перешли куда-то еще - возможно авторизованы
                # Возвращаемся на главную
                main_page.open()
                return True
                
        except Exception as e:
            print(f"Ошибка при проверке авторизации: {e}")
            return False

    @staticmethod
    @allure.step("Выйти из системы")
    def logout(driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        login_page = LoginPage(driver)

        # Ждем исчезновения оверлеев
        main_page.wait_for_no_overlay()
        
        # Переходим в личный кабинет
        main_page.click_personal_account()
        account_page.wait_for_page_loaded()

        # Проверяем что мы на странице аккаунта
        if account_page.is_current_page():
            account_page.click_logout()
            login_page.wait_for_page_loaded()
            return login_page
        else:
            # Если не попали на страницу аккаунта, возвращаем текущую страницу
            return main_page

    @staticmethod
    @allure.step("Перейти в личный кабинет")
    def go_to_personal_account(driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        # Ждем исчезновения оверлеев
        main_page.wait_for_no_overlay()
        
        # Переходим в личный кабинет
        main_page.click_personal_account()
        account_page.wait_for_page_loaded()
        return account_page