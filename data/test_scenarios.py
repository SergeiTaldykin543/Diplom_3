class TestScenarios:
    """Test scenarios for different application states"""
    
    NAVIGATION = {
        "authenticated_user": {
            "personal_account_redirect": "account",
            "constructor_redirect": "stellarburgers",
            "order_feed_redirect": "feed"
        },
        "not_authenticated_user": {
            "personal_account_redirect": "login",
            "constructor_redirect": "stellarburgers", 
            "order_feed_redirect": "feed"
        }
    }
    
    AUTHENTICATION = {
        "valid_credentials": {
            "email": "test_user_215580@yandex.ru",
            "password": "TestPassword123",
            "expected_result": "success"
        },
        "invalid_credentials": {
            "email": "wrong@yandex.ru", 
            "password": "wrongpass",
            "expected_result": "failure"
        }
    }
    
    ORDER_FEED = {
        "counters_visible": ["all_time", "today"],
        "orders_sections": ["in_progress", "ready"]
    }