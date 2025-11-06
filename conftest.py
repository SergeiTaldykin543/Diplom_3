import sys
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", 
                    help="browser to run tests: chrome or firefox")
    parser.addoption("--headless", action="store_true", 
                    help="run tests in headless mode")

@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    
    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
    
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
    
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    from pages.main_page import MainPage
    main_page = MainPage(driver)
    main_page.open()
    return main_page

@pytest.fixture
def authenticated_user(driver, main_page):
    from services.auth_service import AuthService
    from data.working_data import WorkingData
    AuthService.login(driver, WorkingData.EMAIL, WorkingData.PASSWORD)
    return main_page

@pytest.fixture  
def not_authenticated_user(driver):
    from pages.main_page import MainPage
    main_page = MainPage(driver)
    main_page.open()
    return main_page

@pytest.fixture
def api_register_user():
    import requests
    import random
    import string
    from data.test_data import TestData

    random_suffix = ''.join(random.choices(string.digits, k=6))
    user_data = {
        "email": f"api_user_{random_suffix}@yandex.ru",
        "password": "ApiPassword123",
        "name": f"API_User_{random_suffix}"
    }
    
    url = f"{TestData.BASE_URL}/api/auth/register"
    response = requests.post(url, json=user_data, timeout=10)
    
    if response.status_code == 200:
        user_data['access_token'] = response.json().get('accessToken')
        yield user_data
        
        delete_url = f"{TestData.BASE_URL}/api/auth/user"
        headers = {'Authorization': f"Bearer {user_data['access_token']}"}
        requests.delete(delete_url, headers=headers, timeout=10)
    else:
        yield None

@pytest.fixture
def authenticated_user(driver):
    from services.auth_service import AuthService
    from data.working_data import WorkingData
    from pages.account_page import AccountPage
    
    AuthService.login(driver, WorkingData.EMAIL, WorkingData.PASSWORD)
    account_page = AuthService.go_to_personal_account(driver)
    return account_page