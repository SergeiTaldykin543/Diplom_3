from selenium.webdriver.common.by import By


class MainPageLocators:
    # Header navigation
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[.//p[text()='Конструктор']]")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[.//p[text()='Лента Заказов']]")
    ACCOUNT_BUTTON = (By.XPATH, "//a[.//p[text()='Личный Кабинет']]")
    
    # Constructor sections
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")
    
    # Ingredients
    INGREDIENT_ITEM = (By.CLASS_NAME, "BurgerIngredient_ingredient__1TVf6")
    INGREDIENT_COUNTER = (By.CLASS_NAME, "counter_counter__num__3nue1")
    INGREDIENT_PRICE = (By.CLASS_NAME, "BurgerIngredient_ingredient__price__3p5Rm")
    
    # Constructor area
    CONSTRUCTOR_AREA = (By.CLASS_NAME, "BurgerConstructor_basket__listContainer__3P_AM")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    ORDER_TOTAL = (By.CLASS_NAME, "BurgerConstructor_basket__totalContainer__2Z-ho")
    
    # Login
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    
    # Modal windows
    MODAL_OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
    MODAL_CONTENT = (By.CLASS_NAME, "Modal_modal__contentBox__sCy8X")
    MODAL_CLOSE_BUTTON = (By.CLASS_NAME, "Modal_modal__close__TnseK")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title__2L34m')]")


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")