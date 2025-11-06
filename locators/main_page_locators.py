from selenium.webdriver.common.by import By

class MainPageLocators:
    # Header
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    
    # Logo
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    
    # Ingredients sections
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")
    FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")
    
    # Ingredients
    INGREDIENT_ITEM = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__')]")
    INGREDIENT_COUNTER = (By.XPATH, ".//div[contains(@class, 'counter_counter__')]")
    INGREDIENT_PRICE = (By.XPATH, ".//p[contains(@class, 'BurgerIngredient_ingredient__price__')]")
    INGREDIENT_NAME = (By.XPATH, ".//p[contains(@class, 'BurgerIngredient_ingredient__text__')]")
    
    # Constructor area
    CONSTRUCTOR_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_TOTAL = (By.XPATH, "//p[contains(@class, 'BurgerConstructor_burgerConstructor__total')]//span")
    
    # Modal windows
    INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__')]")
    MODAL_INGREDIENT_NAME = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title__')]")
    MODAL_INGREDIENT_DETAILS = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox__')]")
    
    # Order modal
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title__')]")