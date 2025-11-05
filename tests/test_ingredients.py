import pytest
import allure


class TestIngredientsInteraction:
    """Тесты взаимодействия с ингредиентами"""
    
    @allure.title("Открытие модального окна с деталями ингредиента")
    def test_open_ingredient_modal(self, authenticated_user):
        authenticated_user.click_ingredient()
        assert authenticated_user.is_modal_displayed()

    @allure.title("Закрытие модального окна ингредиента")
    def test_close_ingredient_modal(self, authenticated_user):
        authenticated_user.click_ingredient()
        assert authenticated_user.is_modal_displayed()
        
        authenticated_user.close_modal()
        authenticated_user.wait_for_element_to_disappear(authenticated_user.locators.MODAL_CONTENT)

    @allure.title("Увеличение счетчика ингредиента при добавлении")
    def test_ingredient_counter_increases(self, authenticated_user):
        initial_counter = authenticated_user.get_ingredient_counter()
        authenticated_user.add_ingredient_to_constructor()
        new_counter = authenticated_user.get_ingredient_counter()
        
        assert new_counter > initial_counter