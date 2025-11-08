class URLs:
    BASE_URL = "https://stellarburgers.education-services.ru"
    
    # UI URLs
    MAIN_PAGE = f"{BASE_URL}/"
    LOGIN_PAGE = f"{BASE_URL}/login"
    REGISTER_PAGE = f"{BASE_URL}/register"
    FORGOT_PASSWORD_PAGE = f"{BASE_URL}/forgot-password"
    RESET_PASSWORD_PAGE = f"{BASE_URL}/reset-password"
    PROFILE_PAGE = f"{BASE_URL}/account/profile"
    ORDER_FEED_PAGE = f"{BASE_URL}/feed"
    
    # API Endpoints
    API_REGISTER = f"{BASE_URL}/api/auth/register"
    API_LOGIN = f"{BASE_URL}/api/auth/login"
    API_USER = f"{BASE_URL}/api/auth/user"
    API_LOGOUT = f"{BASE_URL}/api/auth/logout"