from selenium.webdriver.common.by import By


class OrderFeedLocators:
    # Order statistics
    TOTAL_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
    
    # Orders in progress
    ORDERS_IN_PROGRESS_SECTION = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__')]")
    ORDERS_IN_PROGRESS_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__')]//li")
    
    # Order cards
    ORDER_CARDS = (By.CLASS_NAME, "OrderHistory_listItem__2x95r")