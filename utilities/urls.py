from data.test_data import TestData

class URLs:
    BASE_URL = TestData.BASE_URL
    MAIN_PAGE = f"{BASE_URL}/"
    LOGIN_PAGE = f"{BASE_URL}/login"
    REGISTER_PAGE = f"{BASE_URL}/register"
    FORGOT_PASSWORD_PAGE = f"{BASE_URL}/forgot-password"
    RESET_PASSWORD_PAGE = f"{BASE_URL}/reset-password"
    PROFILE_PAGE = f"{BASE_URL}/account/profile"
    ORDER_FEED_PAGE = f"{BASE_URL}/feed"