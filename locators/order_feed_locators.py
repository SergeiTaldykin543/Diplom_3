from selenium.webdriver.common.by import By

class OrderFeedLocators:
    # Order counters
    ORDERS_DONE_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за всё время:']/following-sibling::p")
    ORDERS_DONE_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    
    # Orders in progress
    ORDERS_IN_PROGRESS_SECTION = (By.XPATH, "//div[contains(text(), 'В работе')]/following-sibling::ul")
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList__')]//li")
    
    # Order items
    ORDER_ITEMS = (By.XPATH, "//div[contains(@class, 'OrderHistory_listItem__')]")
    ORDER_NUMBER = (By.XPATH, ".//p[contains(@class, 'OrderHistory_textBox__')]")
    
    # Order details modal
    ORDER_DETAILS_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    ORDER_DETAILS_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title__')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__')]")