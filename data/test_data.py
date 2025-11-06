class TestData:
    BASE_URL = "https://stellarburgers.education-services.ru"
    
    # Тестовые пользователи
    VALID_USER = {
        "email": "test_user_215580@yandex.ru",
        "password": "TestPassword123", 
        "name": "Test_User_215580"
    }
    
    INVALID_USER = {
        "email": "invalid@yandex.ru",
        "password": "WrongPassword123",
        "name": "Invalid_User"
    }
    
    # Тестовые сценарии
    NAVIGATION_SCENARIOS = {
        "constructor_to_feed": {
            "from_page": "constructor",
            "to_page": "order_feed",
            "expected_url_contains": "feed"
        },
        "feed_to_constructor": {
            "from_page": "order_feed", 
            "to_page": "constructor",
            "expected_url_contains": "stellarburgers"
        }
    }
    
    INGREDIENT_SCENARIOS = {
        "bun_ingredient": {"ingredient_index": 0, "ingredient_type": "bun"},
        "sauce_ingredient": {"ingredient_index": 6, "ingredient_type": "sauce"},
        "filling_ingredient": {"ingredient_index": 12, "ingredient_type": "filling"}
    }