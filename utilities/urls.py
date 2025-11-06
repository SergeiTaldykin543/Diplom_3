from data.test_data import TestData

class URLs:
    MAIN_PAGE = TestData.BASE_URL.rstrip('/')  # Убираем слэш в конце
    LOGIN_PAGE = f"{TestData.BASE_URL.rstrip('/')}/login"
    REGISTER_PAGE = f"{TestData.BASE_URL.rstrip('/')}/register"
    FORGOT_PASSWORD_PAGE = f"{TestData.BASE_URL.rstrip('/')}/forgot-password"
    PROFILE_PAGE = f"{TestData.BASE_URL.rstrip('/')}/account/profile"
    ORDER_FEED_PAGE = f"{TestData.BASE_URL.rstrip('/')}/feed"
    
    # API endpoints
    API_LOGIN = f"{TestData.BASE_URL.rstrip('/')}/api/auth/login"
    API_REGISTER = f"{TestData.BASE_URL.rstrip('/')}/api/auth/register"
    API_USER = f"{TestData.BASE_URL.rstrip('/')}/api/auth/user"
    API_ORDERS = f"{TestData.BASE_URL.rstrip('/')}/api/orders"
    API_INGREDIENTS = f"{TestData.BASE_URL.rstrip('/')}/api/ingredients"