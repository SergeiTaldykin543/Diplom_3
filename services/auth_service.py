import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.account_page import AccountPage
from data.test_data import TestData


class AuthService:

    @staticmethod
    @allure.step("Авторизовать пользователя")
    def login(driver, email=TestData.VALID_USER["email"], password=TestData.VALID_USER["password"]):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        login_page.open()
        login_page.wait_for_page_loaded()
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login_button()
        main_page.wait_for_page_loaded(timeout=15)
        
        return main_page

    @staticmethod
    @allure.step("Перейти в личный кабинет")
    def go_to_personal_account(driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        if not main_page.is_current_page():
            main_page.open()
            
        main_page.wait_for_no_overlay()
        main_page.click_personal_account()
        account_page.wait_for_page_loaded()
        
        return account_page

    @staticmethod
    @allure.step("Выйти из системы")
    def logout(driver):
        account_page = AccountPage(driver)
        login_page = LoginPage(driver)

        account_page.wait_for_no_overlay()
        account_page.click_logout()
        login_page.wait_for_page_loaded()
        return login_page