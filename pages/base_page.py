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
        """Открывает страницу по URL"""
        self.driver.get(self.url)
        self.wait_for_page_loaded()
        return self

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Найти элементы {locator}")
    def find_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Кликнуть на элемент {locator}")
    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    @allure.step("Кликнуть на элемент с помощью JavaScript {locator}")
    def click_js(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввести текст '{text}' в элемент {locator}")
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator):
        element = self.find_element(locator)
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
        """Ждет полной загрузки страницы"""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
            return True
        except TimeoutException:
            print(f"⚠️ Страница не загрузилась за {timeout} секунд")
            return False

    @allure.step("Ожидание изменения URL")
    def wait_for_url_change(self, original_url, timeout=10):
        """Ждет изменения URL с исходного значения"""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.current_url != original_url
            )
            return True
        except TimeoutException:
            print(f"⚠️ URL не изменился за {timeout} секунд")
            return False

    @allure.step("Ожидание появления URL содержащего текст")
    def wait_for_url_contains(self, text, timeout=10):
        """Ждет появления текста в URL"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(text)
            )
            return True
        except TimeoutException:
            print(f"⚠️ URL не содержит '{text}' за {timeout} секунд")
            return False

    @allure.step("Ожидание исчезновения элемента")
    def wait_for_element_to_disappear(self, locator, timeout=10):
        """Ждет исчезновения элемента"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            print(f"⚠️ Элемент не исчез за {timeout} секунд")
            return False

    @allure.step("Ожидание отсутствия перекрывающих элементов")
    def wait_for_no_overlay(self, timeout=10):
        """Ждет исчезновения перекрывающих элементов (модальных окон)"""
        try:
        # Ждем исчезновения модальных окон или оверлеев
            WebDriverWait(self.driver, timeout).until(
                lambda driver: len(driver.find_elements(By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")) == 0
          )
            return True
        except TimeoutException:
            print("⚠️ Модальное окно все еще присутствует после ожидания")
            return False