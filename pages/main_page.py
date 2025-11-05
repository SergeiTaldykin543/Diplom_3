from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.main_page_locators import LoginPageLocators
import allure


class MainPage(BasePage):
    
    @allure.step("Кликнуть на 'Конструктор'")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на 'Лента заказов'")
    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Кликнуть на 'Личный кабинет'")
    def click_account(self):
        self.click(MainPageLocators.ACCOUNT_BUTTON)

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self, index=0):
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        ingredients[index].click()

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Проверить отображение модального окна")
    def is_modal_displayed(self):
        return self.is_element_visible(MainPageLocators.MODAL_CONTENT)

    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self, ingredient_index=0):
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        self.drag_and_drop(MainPageLocators.INGREDIENT_ITEM, MainPageLocators.CONSTRUCTOR_AREA)

    @allure.step("Получить счетчик ингредиента")
    def get_ingredient_counter(self, index=0):
        try:
            counters = self.find_elements(MainPageLocators.INGREDIENT_COUNTER, timeout=5)
            if counters and index < len(counters):
                return int(counters[index].text) if counters[index].text else 0
            return 0
        except:
            return 0

    @allure.step("Оформить заказ")
    def place_order(self):
        self.click(MainPageLocators.ORDER_BUTTON)

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        initial_text = self.get_text(MainPageLocators.ORDER_NUMBER)
        return self.wait_for_text_to_change(
            MainPageLocators.ORDER_NUMBER, 
            initial_text,
            timeout=30
        )

    @allure.step("Войти в аккаунт через главную страницу")
    def login_from_main_page(self, email, password):
        self.click(MainPageLocators.LOGIN_BUTTON)
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Войти в аккаунт через личный кабинет")
    def login_via_account(self, email, password):
        self.click_account()
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Проверить авторизацию пользователя")
    def is_user_logged_in(self):
        return not self.is_element_visible(MainPageLocators.LOGIN_BUTTON, timeout=3)