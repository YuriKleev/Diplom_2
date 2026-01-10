import pytest
import allure

from conftest import new_user_data, user_with_valid_data

from methods import Methods
from status_codes import HTTPStatusCodes

class TestCreateUser:

    @allure.title("Проверка возможности создания уникального пользователя")
    @allure.description(
        f"Проверяем успешное создание пользователя с валидными данными\n"
        f"Ожидаемый результат: код 200 ОК"
    )
    def test_create_unique_user_success(self, new_user_data):
        response = Methods.create_user(new_user_data)
        response_data = response.json()
        auth_token = response_data['accessToken']

        assert response.status_code == HTTPStatusCodes.CODE_200_OK['status_code']
        assert response_data['success'] == HTTPStatusCodes.CODE_200_OK['success']
        assert 'accessToken' in response_data
        assert 'refreshToken' in response_data
        assert response_data['user']['email'] == new_user_data['email']
        assert response_data['user']['name'] == new_user_data['name']

        Methods.delete_user(auth_token)


    @allure.title("Проверка возможности создания пользователей с одинаковыми данными")
    @allure.description(
        f"Проверяем, что при попытке создать пользователя с логином, который уже есть, возвращается ошибка\n"
        f"Ожидаемый результат: код 403 Forbidden"
    )
    def test_create_two_same_users_failed(self, user_with_valid_data):
        first_user_response = Methods.create_user(user_with_valid_data)
        first_user_response_data = first_user_response.json()
        auth_token = first_user_response_data['accessToken']
        second_user_response = Methods.create_user(user_with_valid_data)

        assert second_user_response.status_code == HTTPStatusCodes.CREATE_EXISTING_USER_CODE_403_FORBIDDEN['status_code']
        assert second_user_response.json()['success'] == HTTPStatusCodes.CREATE_EXISTING_USER_CODE_403_FORBIDDEN['success']
        assert second_user_response.json()['message'] == HTTPStatusCodes.CREATE_EXISTING_USER_CODE_403_FORBIDDEN['message']

        Methods.delete_user(auth_token)


    @allure.title("Проверка возможности создания пользователя с незаполненными обязательными полями")
    @pytest.mark.parametrize('empty_field', ['email', 'password', 'name'])
    def test_create_user_with_empty_fields_failed(self, user_with_valid_data, empty_field):
        allure.dynamic.description(
            f"Проверяем, что при попытке создать пользователя с незаполненным полем {empty_field} возвращается ошибка\n"
            f"Ожидаемый результат: код 403 Forbidden"    
        )
        user_data = user_with_valid_data
        user_data[empty_field] = ''
        response = Methods.create_user(user_data)
        response_data = response.json()

        assert response.status_code == HTTPStatusCodes.CREATE_USER_WITH_EMPTY_FIELDS_CODE_403_FORBIDDEN['status_code']
        assert response_data['success'] == HTTPStatusCodes.CREATE_USER_WITH_EMPTY_FIELDS_CODE_403_FORBIDDEN['success']
        assert response_data['message'] == HTTPStatusCodes.CREATE_USER_WITH_EMPTY_FIELDS_CODE_403_FORBIDDEN['message']
