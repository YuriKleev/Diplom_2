import allure

from conftest import new_user_data

from helper import generate_random_ingredient_id

from methods import Methods
from status_codes import HTTPStatusCodes

class TestMakeOrder:

    @allure.title("Проверка возможности создания заказа авторизованным пользователем")
    @allure.description(
        f"Проверяем успешное создание заказа авторизованным пользователем.\n"
        f"Проверка объединена с проверкой создания заказа с ингредиентами.\n"
        f"Ожидаемый результат: код 200 OK"
    )
    def test_make_order_by_authorized_user_success(self, new_user_data, ingredients):
        response = Methods.create_user(new_user_data)
        response_data = response.json()
        auth_token = response_data['accessToken']
        ingredient_list = [ingredients[0]['_id'], ingredients[1]['_id']]
        order_response = Methods.make_order(ingredient_list, auth_token)
        order_response_data = order_response.json()

        assert order_response.status_code == HTTPStatusCodes.MAKE_ORDER_CODE_200_OK['status_code']
        assert order_response_data['success'] == HTTPStatusCodes.MAKE_ORDER_CODE_200_OK['success']
        assert 'name' in order_response_data
        assert 'order' in order_response_data
        assert 'number' in order_response_data['order']
        
        Methods.delete_user(auth_token)


    @allure.title("Проверка возможности создания заказа неавторизованным пользователем")
    @allure.description(
        f"Проверяем создание заказа неавторизованным пользователем.\n"
        f"Согласно пояснениям наставника, ожидаем код 200 ОК, хоть это и противоречит документации.\n"
        f"Ожидаемый результат: код 200 OK"
    )
    def test_make_order_by_unauthorized_user_success(self, ingredients):
        ingredient_list = [ingredients[0]['_id'], ingredients[1]['_id']]
        order_response = Methods.make_order(ingredient_list)
        order_response_data = order_response.json()

        assert order_response.status_code == HTTPStatusCodes.MAKE_ORDER_CODE_200_OK['status_code']
        assert order_response_data['success'] == HTTPStatusCodes.MAKE_ORDER_CODE_200_OK['success']
        assert 'name' in order_response_data
        assert 'order' in order_response_data
        assert 'number' in order_response_data['order']


    @allure.title("Проверка возможности создания заказа без ингредиентов")
    @allure.description(
        f"Проверяем неуспешное создание заказа без ингредиентов\n"
        f"Ожидаемый результат: код 400 Bad Request"
    )
    def test_make_order_without_ingredients_failed(self, new_user_data):
        response = Methods.create_user(new_user_data)
        response_data = response.json()
        auth_token = response_data['accessToken']
        ingredient_list = []
        order_response = Methods.make_order(ingredient_list, auth_token)
        order_response_data = order_response.json()

        assert order_response.status_code == HTTPStatusCodes.MAKE_ORDER_WITHOUT_INGREDIENTS_CODE_400_BAD_REQUEST['status_code']
        assert order_response_data['success'] == HTTPStatusCodes.MAKE_ORDER_WITHOUT_INGREDIENTS_CODE_400_BAD_REQUEST['success']
        assert order_response_data['message'] == HTTPStatusCodes.MAKE_ORDER_WITHOUT_INGREDIENTS_CODE_400_BAD_REQUEST['message']
        
        Methods.delete_user(auth_token)


    @allure.title("Проверка возможности создания заказа с неверным хешем ингредиентов")
    @allure.description(
        f"Проверяем неуспешное создание заказа с неверным хешем ингредиентов\n"
        f"Ожидаемый результат: код 500 Internal Server Error"
    )
    def test_make_with_wrong_ingredients_hash_failed(self, new_user_data):
        response = Methods.create_user(new_user_data)
        response_data = response.json()
        auth_token = response_data['accessToken']
        ingredient_list = [generate_random_ingredient_id(24)]
        order_response = Methods.make_order(ingredient_list, auth_token)

        assert order_response.status_code == HTTPStatusCodes.MAKE_ORDER_WRONG_HASH_CODE_500_SERVER_ERROR['status_code']
        assert HTTPStatusCodes.MAKE_ORDER_WRONG_HASH_CODE_500_SERVER_ERROR['text'] in order_response.text

        Methods.delete_user(auth_token)
