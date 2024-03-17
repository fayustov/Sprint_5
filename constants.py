import faker


class Constants:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'
    REGISTRATION_URL = 'https://stellarburgers.nomoreparties.site/register'
    LOGIN_URL = 'https://stellarburgers.nomoreparties.site/login'
    FORGOT_PASSWORD_URL = 'https://stellarburgers.nomoreparties.site/forgot-password'
    PROFILE_URL = 'https://stellarburgers.nomoreparties.site/account/profile'
    BASE_USER = {
        "name": "Testik Testovich",
        "email": "etoya@sofiarotaru.com",
        "password": "123456"
    }
    CORRECT_USER_DATA = {
        "name": faker.Faker().name(),
        "email": faker.Faker().email(),
        "password": faker.Faker().password()
    }
    INCORRECT_USER_DATA = {
        "name": "Имя",
        "email": "test@email.com",
        "password": "12345"
    }
