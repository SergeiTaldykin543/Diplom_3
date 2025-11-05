import pytest
import allure


class TestOrderCreation:
    """Тесты создания заказов"""
    
    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, authenticated_user):
        authenticated_user.add_ingredient_to_constructor(0)
        authenticated_user.add_ingredient_to_constructor(5)
        
        authenticated_user.place_order()
        order_number = authenticated_user.get_order_number()
        
        assert order_number.isdigit()
        assert order_number != "9999"
        
        authenticated_user.close_modal()

    @allure.title("Отображение модального окна при создании заказа")
    def test_order_modal_displayed(self, authenticated_user):
        authenticated_user.add_ingredient_to_constructor(0)
        authenticated_user.place_order()
        
        assert authenticated_user.is_modal_displayed()
        authenticated_user.close_modal()