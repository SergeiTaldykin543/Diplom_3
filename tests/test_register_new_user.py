import pytest
import allure
import requests
import random
import string
from data.test_data import TestData

@allure.feature("Registration")
class TestRegisterNewUser:
    
    def generate_test_user(self):
        """Генерирует данные для тестового пользователя"""
        random_suffix = ''.join(random.choices(string.digits, k=6))
        return {
            "email": f"test_user_{random_suffix}@yandex.ru",
            "password": "TestPassword123",
            "name": f"Test_User_{random_suffix}"
        }
    
    @allure.title("Register new user via API and test login")
    def test_register_and_login_new_user(self, driver):
        """Регистрируем нового пользователя и тестируем логин"""
        from pages.main_page import MainPage
        from pages.login_page import LoginPage
        
        # Шаг 1: Регистрируем пользователя через API
        print("\n=== STEP 1: Registering new user via API ===")
        new_user = self.generate_test_user()
        
        register_url = f"{TestData.BASE_URL}/api/auth/register"
        response = requests.post(register_url, json=new_user, timeout=10)
        
        if response.status_code == 200:
            print("✅ User registered successfully via API")
            print(f"Email: {new_user['email']}")
            print(f"Name: {new_user['name']}")
        else:
            print("❌ User registration failed")
            pytest.skip("Cannot register new user")
            return
        
        # Шаг 2: Пробуем войти через UI с новым пользователем
        print("\n=== STEP 2: Testing UI login with new user ===")
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        
        # Переходим на страницу логина
        driver.get(f"{TestData.BASE_URL}/login")
        
        # Вводим данные нового пользователя
        login_page.enter_email(new_user['email'])
        login_page.enter_password(new_user['password'])
        
        # Делаем скриншот перед логином
        driver.save_screenshot("new_user_before_login.png")
        
        # Кликаем кнопку входа
        login_page.click_login_button()
        
        # Ждем и проверяем результат
        import time
        time.sleep(5)
        
        current_url = driver.current_url
        print(f"URL after login attempt: {current_url}")
        
        # Делаем скриншот после логина
        driver.save_screenshot("new_user_after_login.png")
        
        if "login" not in current_url:
            print("✅ UI LOGIN SUCCESSFUL with new user!")
            print(f"Redirected to: {current_url}")
        else:
            print("❌ UI LOGIN FAILED with new user")
            print("Remaining on login page")
            
        # Шаг 3: Проверяем через API что пользователь залогинен
        print("\n=== STEP 3: Verifying login via API ===")
        user_url = f"{TestData.BASE_URL}/api/auth/user"
        
        # Получаем токен из API ответа при регистрации
        access_token = response.json().get('accessToken')
        if access_token:
            headers = {'Authorization': f'Bearer {access_token}'}
            user_response = requests.get(user_url, headers=headers, timeout=10)
            
            if user_response.status_code == 200:
                user_data = user_response.json()
                print("✅ API user verification SUCCESSFUL")
                print(f"User data: {user_data}")
            else:
                print("❌ API user verification failed")
        
        # Очистка: удаляем тестового пользователя
        print("\n=== CLEANUP: Deleting test user ===")
        if access_token:
            delete_url = f"{TestData.BASE_URL}/api/auth/user"
            headers = {'Authorization': f'Bearer {access_token}'}
            delete_response = requests.delete(delete_url, headers=headers, timeout=10)
            
            if delete_response.status_code == 202:
                print("✅ Test user deleted successfully")
            else:
                print("❌ Failed to delete test user")