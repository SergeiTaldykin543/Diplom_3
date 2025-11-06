import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.account_page import AccountPage


class AuthService:
    
    @staticmethod
    @allure.step("Авторизовать пользователя")
    def login(driver, email, password):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        
        login_page.open()
        login_page.login(email, password)
        main_page.wait_for_page_loaded()
        
        return main_page
    
    @staticmethod
    @allure.step("Выйти из системы")
    def logout(driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        login_page = LoginPage(driver)
        
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
        
        main_page.click_personal_account()
        account_page.wait_for_page_loaded()
        
        return account_page