from utilities.urls import URLs

class NavigationScenarios:
    CONSTRUCTOR_TO_FEED = {
        "start_page": "constructor",
        "action": "click_order_feed", 
        "expected_page": "order_feed",
        "expected_url": URLs.ORDER_FEED_PAGE
    }
    
    FEED_TO_CONSTRUCTOR = {
        "start_page": "order_feed",
        "action": "click_constructor", 
        "expected_page": "constructor",
        "expected_url": URLs.MAIN_PAGE
    }
    
    TO_PERSONAL_ACCOUNT = {
        "start_page": "constructor",
        "action": "click_personal_account",
        "expected_page": "account", 
        "expected_url": URLs.PROFILE_PAGE
    }


class UserActionScenarios:
    LOGOUT = {
        "start_page": "account",
        "action": "click_logout",
        "expected_page": "login",
        "expected_url": URLs.LOGIN_PAGE
    }
    
    NAVIGATE_VIA_LOGO = {
        "start_page": "account", 
        "action": "click_logo",
        "expected_page": "constructor",
        "expected_url": URLs.MAIN_PAGE
    }
    
    NAVIGATE_VIA_CONSTRUCTOR = {
        "start_page": "account",
        "action": "click_constructor", 
        "expected_page": "constructor",
        "expected_url": URLs.MAIN_PAGE
    }


class IngredientScenarios:
    OPEN_MODAL = {
        "action": "click_ingredient",
        "expected_result": "modal_visible"
    }
    
    CLOSE_MODAL = {
        "action": "close_modal", 
        "expected_result": "modal_closed"
    }


class OrderFeedScenarios:
    CHECK_COUNTERS = {
        "action": "check_counters",
        "expected_result": "counters_displayed"
    }
    
    CHECK_IN_PROGRESS = {
        "action": "check_in_progress",
        "expected_result": "section_accessible"
    }