from .test_data import TestData

class URLs:
    MAIN_PAGE = TestData.BASE_URL
    LOGIN_PAGE = f"{TestData.BASE_URL}/login"
    PROFILE_PAGE = f"{TestData.BASE_URL}/account/profile"
    ORDER_FEED_PAGE = f"{TestData.BASE_URL}/feed"
    REGISTER_PAGE = f"{TestData.BASE_URL}/register"
    FORGOT_PASSWORD_PAGE = f"{TestData.BASE_URL}/forgot-password"
    RESET_PASSWORD_PAGE = f"{TestData.BASE_URL}/reset-password"