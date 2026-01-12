import pytest
import allure

from conftest import new_user_data

from methods import Methods
from status_codes import HTTPStatusCodes

class TestLoginUser:

    @allure.title("Проверка возможности логина пользователя")
    @allure.description(
        f"Проверяем успешный логин пользователя с валидными данными\n"
        f"Ожидаемый результат: код 200 OK"
    )
    def test_login_existing_user_success(self, new_user_data):
        response_register = Methods.create_user(new_user_data)
        login_payload = {
            'email': new_user_data['email'],
            'password': new_user_data['password']
        }
        response_login = Methods.login_user(login_payload)
        response_login_data = response_login.json()

        assert response_login.status_code == HTTPStatusCodes.CODE_200_OK['status_code']
        assert response_login_data['success'] == HTTPStatusCodes.CODE_200_OK['success']
        assert 'accessToken' in response_login_data
        assert 'refreshToken' in response_login_data
        assert response_login_data['user']['email'] == new_user_data['email']
        assert response_login_data['user']['name'] == new_user_data['name']

        auth_token = response_register.json()['accessToken']
        Methods.delete_user(auth_token)


    @allure.title("Проверка возможности логина пользователя с неправильно заполненными почтой или паролем")
    @pytest.mark.parametrize('field', ['email', 'password'])
    def test_login_user_with_wrong_fields_failed(self, new_user_data, field):
        allure.dynamic.description(
            f"Проверяем, что при попытке логина пользователя с неправильно заполненным полем {field} возвращается ошибка\n"
            f"Ожидаемый результат: код 401 Unauthorized"
        )
        response_register = Methods.create_user(new_user_data)
        login_payload = {
            'email': new_user_data['email'],
            'password': new_user_data['password']
        }
        login_payload[field] = f"wrong{field}"
        response_login = Methods.login_user(login_payload)
        response_login_data = response_login.json()
        
        assert response_login.status_code == HTTPStatusCodes.LOGIN_WRONG_DATA_CODE_401_UNAUTHORIZED['status_code']
        assert response_login_data['success'] == HTTPStatusCodes.LOGIN_WRONG_DATA_CODE_401_UNAUTHORIZED['success']
        assert response_login_data['message'] == HTTPStatusCodes.LOGIN_WRONG_DATA_CODE_401_UNAUTHORIZED['message']

        auth_token = response_register.json()['accessToken']
        Methods.delete_user(auth_token)
