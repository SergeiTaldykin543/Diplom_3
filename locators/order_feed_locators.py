from selenium.webdriver.common.by import By

class OrderFeedLocators:
    # Order counters
    ORDERS_DONE_ALL_TIME = (By.XPATH, "//p[contains(text(), 'Выполнено за всё время')]/following-sibling::p")
    ORDERS_DONE_TODAY = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
    
    # Orders in progress
    ORDERS_IN_PROGRESS_SECTION = (By.XPATH, "//div[contains(text(), 'В работе')]")
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]//li")
    
    # Order items
    ORDER_ITEMS = (By.XPATH, "//div[contains(@class, 'OrderHistory_listItem') or contains(@class, 'OrderFeed_orderItem')]")
    ORDER_NUMBER = (By.XPATH, ".//p[contains(@class, 'textBox') or contains(@class, 'orderNumber')]")
    
    # Order details modal
    ORDER_DETAILS_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    ORDER_DETAILS_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")