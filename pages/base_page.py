from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def find_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
    
    def click(self, locator):
        element = self.find_element(locator)
        element.click()
    
    def get_text(self, locator):
        return self.find_element(locator).text
    
    def wait_for_element_to_disappear(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))
    
    def is_element_visible(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False
    
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)