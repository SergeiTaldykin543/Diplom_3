from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import allure


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу")
    def open(self):
        self.driver.get(self.url)
        self.wait_for_page_loaded()
        return self

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получить имя браузера")
    def get_browser_name(self):
        return self.driver.name.lower()

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Найти элементы {locator}")
    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    @allure.step("Кликнуть на элемент {locator}")
    def click(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        
        # Универсальный клик для всех браузеров
        if "firefox" in self.get_browser_name():
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    @allure.step("Кликнуть на элемент с помощью JavaScript {locator}")
    def click_js(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввести текст в элемент {locator}")
    def send_keys(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.text

    @allure.step("Ожидание видимости элемента {locator}")
    def wait_for_element_to_be_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Проверить видимость элемента {locator}")
    def is_element_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Ожидание загрузки страницы")
    def wait_for_page_loaded(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Ожидание изменения URL")
    def wait_for_url_change(self, original_url, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.current_url != original_url
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Ожидание отсутствия перекрывающих элементов")
    def wait_for_no_overlay(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: len(driver.find_elements(By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")) == 0
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Ожидание исчезновения элемента")
    def wait_for_element_to_disappear(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False