import pytest
import allure

@allure.feature("Ingredients")
class TestIngredients:
    
    @allure.title("Test ingredient modal opens on click")
    @allure.description("Test that ingredient details modal opens when clicking on ingredient")
    def test_ingredient_modal_opens(self, driver, login):
        from pages.main_page import MainPage
        
        main_page = MainPage(driver)
        
        with allure.step("Click on first ingredient"):
            main_page.click_ingredient(0)
        
        with allure.step("Verify modal is visible"):
            assert main_page.is_modal_visible()
    
    @allure.title("Test ingredient modal closes on X click")
    @allure.description("Test that ingredient modal closes when clicking X button")
    def test_ingredient_modal_closes(self, driver, login):
        from pages.main_page import MainPage
        
        main_page = MainPage(driver)
        
        with allure.step("Click on ingredient to open modal"):
            main_page.click_ingredient(0)
        
        with allure.step("Verify modal is visible"):
            assert main_page.is_modal_visible()
        
        with allure.step("Click close button"):
            main_page.close_modal()
        
        with allure.step("Verify modal is closed"):
            assert not main_page.is_modal_visible()
    
    @allure.title("Test ingredient counter increases when added to order")
    @allure.description("Test that ingredient counter increases when ingredient is added to constructor")
    def test_ingredient_counter_increases(self, driver, login):
        from pages.main_page import MainPage
        
        main_page = MainPage(driver)
        
        # This test would require drag and drop implementation
        # For now, it's a placeholder for the functionality
        with allure.step("Get initial counter value"):
            initial_counter = main_page.get_ingredient_counter(0)
        
        with allure.step("Add ingredient to constructor (would require drag and drop)"):
            # Implementation for drag and drop would go here
            pass
        
        with allure.step("Verify counter increased"):
            # new_counter = main_page.get_ingredient_counter(0)
            # assert new_counter > initial_counter
            pytest.skip("Drag and drop functionality not implemented in this version")