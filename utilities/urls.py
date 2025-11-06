from data.working_data import WorkingData

class URLs:
    MAIN_PAGE = WorkingData.BASE_URL
    LOGIN_PAGE = f"{WorkingData.BASE_URL}/login"
    REGISTER_PAGE = f"{WorkingData.BASE_URL}/register"
    FORGOT_PASSWORD_PAGE = f"{WorkingData.BASE_URL}/forgot-password"
    PROFILE_PAGE = f"{WorkingData.BASE_URL}/account/profile"
    ORDER_FEED_PAGE = f"{WorkingData.BASE_URL}/feed"