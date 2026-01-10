MAIN_PAGE_URL='https://stellarburgers.education-services.ru'

class Endpoints:

    CREATE_ACCOUNT_ENDPOINT = f"{MAIN_PAGE_URL}/api/auth/register"
    LOGIN_ACCOUNT_ENDPOINT = f"{MAIN_PAGE_URL}/api/auth/login"
    DELETE_ACCOUNT_ENDPOINT = f"{MAIN_PAGE_URL}/api/auth/user"
    MAKE_ORDER_ENDPOINT = f"{MAIN_PAGE_URL}/api/orders"
    GET_INGREDIENTS_INFO_ENDPOINT = f"{MAIN_PAGE_URL}/api/ingredients"
