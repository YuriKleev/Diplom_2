class HTTPStatusCodes:

    CODE_200_OK = {
        'status_code': 200,
        'success': True,
        'message': 'accessToken'
    }

    CREATE_EXISTING_USER_CODE_403_FORBIDDEN = {
        'status_code': 403,
        'success': False,
        'message': 'User already exists'
    }

    CREATE_USER_WITH_EMPTY_FIELDS_CODE_403_FORBIDDEN = {
        'status_code': 403,
        'success': False,
        'message': 'Email, password and name are required fields'
    }

    LOGIN_WRONG_DATA_CODE_401_UNAUTHORIZED = {
        'status_code': 401,
        'success': False,
        'message': 'email or password are incorrect'
    }

    MAKE_ORDER_CODE_200_OK = {
        'status_code': 200,
        'success': True,
        'message': 'order'
    }

    MAKE_ORDER_WITHOUT_INGREDIENTS_CODE_400_BAD_REQUEST = {
        'status_code': 400,
        'success': False,
        'message': 'Ingredient ids must be provided'
    }

    MAKE_ORDER_WRONG_HASH_CODE_500_SERVER_ERROR = {
        'status_code': 500,
        'text': 'Internal Server Error'
    }
