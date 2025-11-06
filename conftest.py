import sys
import os

# Добавляем корневую директорию проекта в PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser to run tests: chrome or firefox")
    parser.addoption("--headless", action="store_true", help="run tests in headless mode")


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    
    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        web_driver = webdriver.Chrome(options=options)
    
    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        web_driver = webdriver.Firefox(options=options)
    
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    web_driver.implicitly_wait(10)
    
    yield web_driver
    web_driver.quit()


@pytest.fixture
def login(driver):
    from services.auth_service import AuthService
    from data.working_data import WorkingData
    
    return AuthService.login(driver, WorkingData.EMAIL, WorkingData.PASSWORD)


@pytest.fixture
def authenticated_user(driver, login):
    from services.auth_service import AuthService
    
    return AuthService.go_to_personal_account(driver)