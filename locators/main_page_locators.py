from selenium.webdriver.common.by import By


class MainPageLocators:
    # Header
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    
    # Ingredients sections
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")
    FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")
    
    # Ingredients - более гибкие локаторы
    INGREDIENT_ITEM = (By.XPATH, "//section[contains(@class, 'BurgerIngredients_ingredients')]//a")
    INGREDIENT_COUNTER = (By.XPATH, ".//div[contains(@class, 'counter')]")
    
    # Constructor area
    CONSTRUCTOR_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    ORDER_TOTAL = (By.XPATH, "//p[contains(@class, 'BurgerConstructor_total')]//span")
    
    # Modal windows
    INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    MODAL_INGREDIENT_NAME = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")