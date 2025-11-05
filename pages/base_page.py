from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Найти элементы {locator}")
    def find_elements(self, locator, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_any_elements_located(locator))

    @allure.step("Найти кликабельный элемент {locator}")
    def find_clickable_element(self, locator, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Кликнуть на элемент {locator}")
    def click(self, locator):
        element = self.find_clickable_element(locator)
        element.click()

    @allure.step("Ввести текст '{text}' в элемент {locator}")
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Проверить видимость элемента {locator}")
    def is_element_visible(self, locator, timeout=5):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Дождаться исчезновения элемента {locator}")
    def wait_for_element_to_disappear(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Дождаться изменения текста элемента {locator}")
    def wait_for_text_to_change(self, locator, initial_text, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        
        def text_changed(driver):
            try:
                current_text = self.find_element(locator).text
                return current_text != initial_text
            except:
                return False
        
        wait.until(text_changed)
        return self.find_element(locator).text

    @allure.step("Перетащить элемент {source} на {target}")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url