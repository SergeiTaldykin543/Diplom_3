class WorkingData:
    BASE_URL = "https://stellarburgers.education-services.ru"
    
    # Данные которые РЕАЛЬНО работают (из успешной регистрации)
    EMAIL = "test_user_215580@yandex.ru"
    PASSWORD = "TestPassword123"
    NAME = "Test_User_215580"
    
    @classmethod
    def get_credentials(cls):
        return {
            "email": cls.EMAIL,
            "password": cls.PASSWORD,
            "name": cls.NAME
        }