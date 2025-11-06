from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
from abc import ABC, abstractmethod


class BasePage(ABC):
    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)

    @abstractmethod
    def is_current_page(self):
        pass

    @allure.step("Открыть страницу")
    def open(self):
        if self.url:
            self.driver.get(self.url)
        self.wait_for_page_loaded()

    @allure.step("Дождаться загрузки страницы")
    def wait_for_page_loaded(self):
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    @allure.step("Найти элемент: {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Найти элементы: {locator}")
    def find_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Кликнуть на элемент: {locator}")
    def click(self, locator):
        element = self.find_element(locator)
        try:
            element.click()
        except:
            # Если обычный клик не работает, используем JavaScript
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Кликнуть через JavaScript: {locator}")
    def click_js(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Ввести текст: {text} в элемент: {locator}")
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Дождаться исчезновения элемента: {locator}")
    def wait_for_element_to_disappear(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Дождаться видимости элемента: {locator}")
    def wait_for_element_to_be_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Проверить видимость элемента: {locator}")
    def is_element_visible(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Проверить что текущая страница корректна")
    def is_current_page(self):
        return self.url in self.get_current_url()

    @allure.step("Обновить страницу")
    def refresh_page(self):
        self.driver.refresh()
        self.wait_for_page_loaded()

    @allure.step("Закрыть все модальные окна")
    def close_all_modals(self):
        # Пытаемся закрыть модальные окна если они есть
        try:
            # Локатор для кнопки закрытия модального окна
            modal_close = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
            close_buttons = self.driver.find_elements(*modal_close)
            for button in close_buttons:
                try:
                    self.driver.execute_script("arguments[0].click();", button)
                except:
                    pass
        except:
            pass

    @allure.step("Дождаться отсутствия перекрывающих элементов")
    def wait_for_no_overlay(self):
        # Ждем пока исчезнут перекрывающие элементы
        try:
            overlay_locator = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
            self.wait.until(EC.invisibility_of_element_located(overlay_locator))
        except:
            # Если нет перекрывающих элементов, продолжаем
            pass