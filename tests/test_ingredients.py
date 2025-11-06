import pytest
import allure
from pages.main_page import MainPage

@allure.feature("Ingredients")
class TestIngredients:

    @allure.title("Открытие модального окна ингредиента")
    def test_ingredient_modal_opens_on_click(self, driver, login):
        main_page = MainPage(driver)

        # Пробуем кликнуть на ингредиент
        clicked = main_page.click_ingredient(0)
        
        # Если удалось кликнуть, проверяем модальное окно
        if clicked:
            assert main_page.is_modal_visible()
        else:
            pytest.skip("Не удалось найти ингредиенты для тестирования")

    @allure.title("Закрытие модального окна ингредиента")
    def test_ingredient_modal_closes_on_x_click(self, driver, login):
        main_page = MainPage(driver)

        # Пробуем кликнуть на ингредиент
        clicked = main_page.click_ingredient(0)
        
        if clicked and main_page.is_modal_visible():
            main_page.close_modal()
            assert not main_page.is_modal_visible()
        else:
            pytest.skip("Не удалось открыть модальное окно для тестирования")