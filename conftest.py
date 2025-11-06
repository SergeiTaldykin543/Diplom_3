import sys
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Добавляем корневую директорию проекта в PYTHONPATH
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
def login(driver, request):
    """Фикстура для авторизации"""
    from services.auth_service import AuthService
    from data.working_data import WorkingData
    from pages.main_page import MainPage
    
    browser = request.config.getoption("--browser")
    
    try:
        print(f"🔄 Попытка авторизации в {browser}...")
        main_page = AuthService.login(driver, WorkingData.EMAIL, WorkingData.PASSWORD)
        return main_page
    except Exception as e:
        print(f"❌ Ошибка авторизации в {browser}: {e}")
        main_page = MainPage(driver)
        main_page.open()
        return main_page

@pytest.fixture
def authenticated_user(driver, login):
    """Фикстура для аутентифицированного пользователя"""
    from services.auth_service import AuthService
    return AuthService.go_to_personal_account(driver)