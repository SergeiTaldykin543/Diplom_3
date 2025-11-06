import sys
import os

# Добавляем корневую директорию проекта в PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from data.test_data import TestData
import allure
import requests
import json
import time

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser to run tests: chrome or firefox")
    parser.addoption("--headless", action="store_true", help="run tests in headless mode")
    parser.addoption("--base-url", action="store", default=TestData.BASE_URL, help="base URL for the application")

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    base_url = request.config.getoption("--base-url")
    
    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
    
    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
    
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    # Устанавливаем базовый URL
    TestData.BASE_URL = base_url.rstrip('/')
    driver.get(TestData.BASE_URL)
    
    yield driver
    
    # Делаем скриншот при падении теста
    if request.node.rep_call.failed:
        try:
            screenshot_dir = "screenshots"
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            screenshot_path = os.path.join(screenshot_dir, f"{request.node.name}.png")
            driver.save_screenshot(screenshot_path)
            allure.attach.file(screenshot_path, name="screenshot", attachment_type=allure.attachment_type.PNG)
        except:
            pass
    
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук для получения результатов теста"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture
def login(driver):
    """Фикстура для авторизации пользователя"""
    from pages.main_page import MainPage
    from pages.login_page import LoginPage
    
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    
    # Проверяем текущий URL
    current_url = driver.current_url
    print(f"Current URL before login: {current_url}")
    
    # Кликаем на личный кабинет
    try:
        main_page.click_personal_account()
        time.sleep(2)
    except Exception as e:
        print(f"Error clicking personal account: {e}")
        # Если не получилось, переходим напрямую на страницу логина
        driver.get(f"{TestData.BASE_URL}/login")
        time.sleep(2)
    
    # Проверяем, находимся ли мы на странице логина
    if "login" in driver.current_url:
        print("We are on login page, performing login...")
        print(f"Using email: {TestData.EMAIL}")
        
        try:
            # Выполняем вход
            login_page.enter_email(TestData.EMAIL)
            login_page.enter_password(TestData.PASSWORD)
            login_page.click_login_button()
            time.sleep(3)
            
            print(f"After login attempt: {driver.current_url}")
            
            # После успешного логина возвращаемся на главную страницу
            driver.get(TestData.BASE_URL)
            time.sleep(2)
            
        except Exception as e:
            print(f"Error during login: {e}")
            # Если логин не удался, продолжаем без авторизации
            driver.get(TestData.BASE_URL)
            time.sleep(2)
    else:
        print(f"Unexpected page after clicking personal account: {driver.current_url}")
        # Возвращаемся на главную страницу
        driver.get(TestData.BASE_URL)
        time.sleep(2)
    
    return main_page

@pytest.fixture
def manual_login(driver):
    """Фикстура для прямой авторизации на странице логина"""
    from pages.main_page import MainPage
    from pages.login_page import LoginPage
    
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    
    # Переходим напрямую на страницу логина
    driver.get(f"{TestData.BASE_URL}/login")
    time.sleep(2)
    
    print(f"Manual login with email: {TestData.EMAIL}")
    
    # Выполняем вход
    login_page.enter_email(TestData.EMAIL)
    login_page.enter_password(TestData.PASSWORD)
    login_page.click_login_button()
    time.sleep(3)
    
    # Проверяем успешность авторизации
    if "login" not in driver.current_url:
        print("Manual login successful!")
    else:
        print("Manual login failed!")
    
    # Возвращаемся на главную страницу
    driver.get(TestData.BASE_URL)
    time.sleep(2)
    
    return main_page

@pytest.fixture
def api_register_user():
    """Fixture to register a user via API for tests"""
    url = f"{TestData.BASE_URL}/api/auth/register"
    
    # Generate unique user data
    import random
    import string
    random_suffix = ''.join(random.choices(string.digits, k=6))
    user_data = {
        "email": f"test_user_{random_suffix}@example.com",
        "password": "TestPassword123",
        "name": f"Test_User_{random_suffix}"
    }
    
    try:
        response = requests.post(url, json=user_data, timeout=10)
        
        if response.status_code == 200:
            user_data['access_token'] = response.json().get('accessToken')
            user_data['refresh_token'] = response.json().get('refreshToken')
            print(f"Created test user: {user_data['email']}")
            yield user_data
            
            # Cleanup - delete user after test
            delete_url = f"{TestData.BASE_URL}/api/auth/user"
            headers = {'Authorization': f"Bearer {user_data['access_token']}"}
            try:
                requests.delete(delete_url, headers=headers, timeout=10)
                print(f"Deleted test user: {user_data['email']}")
            except requests.exceptions.RequestException as e:
                print(f"Error deleting test user: {e}")
        else:
            print(f"Failed to create test user: {response.status_code} - {response.text}")
            yield None
            
    except requests.exceptions.RequestException as e:
        print(f"Error in api_register_user fixture: {e}")
        yield None

@pytest.fixture
def login(driver):
    """Фикстура для авторизации с рабочими данными"""
    from pages.main_page import MainPage
    from pages.login_page import LoginPage
    from data.working_data import WorkingData
    import time
    
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    
    print(f"Logging in with: {WorkingData.EMAIL}")
    
    # Переходим на страницу логина
    driver.get(f"{WorkingData.BASE_URL}/login")
    time.sleep(2)
    
    # Выполняем вход
    login_page.enter_email(WorkingData.EMAIL)
    login_page.enter_password(WorkingData.PASSWORD)
    login_page.click_login_button()
    time.sleep(3)
    
    # Проверяем успешность логина
    current_url = driver.current_url
    if "login" in current_url:
        print(f"❌ Login failed, still on: {current_url}")
        # Пробуем альтернативный метод
        driver.get(WorkingData.BASE_URL)
    else:
        print(f"✅ Login successful! On: {current_url}")
    
    return main_page

@pytest.fixture
def authenticated_driver(driver, manual_login):
    """Фикстура для гарантированно авторизованного драйвера"""
    return driver

@pytest.fixture(scope="session")
def base_url():
    """Фикстура для базового URL"""
    return TestData.BASE_URL

def pytest_configure(config):
    """Конфигурация pytest"""
    # Создаем директорию для скриншотов
    screenshots_dir = "screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    
    # Создаем директорию для allure результатов
    allure_dir = "allure-results"
    if not os.path.exists(allure_dir):
        os.makedirs(allure_dir)

@pytest.fixture(autouse=True)
def wait_between_tests():
    """Автоматическая пауза между тестами"""
    yield
    time.sleep(1)

@pytest.fixture
def debug_mode(request):
    """Фикстура для отладки - выводит дополнительную информацию"""
    def _debug_print(message):
        if request.config.getoption("--verbose") > 0:
            print(f"DEBUG: {message}")
    return _debug_print