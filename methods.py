import requests
import allure
from endpoints import Endpoints

class Methods:

    @staticmethod
    @allure.step('Отправка POST-запроса для регистрации пользователя')
    def create_user(payload):
        return requests.post(url=Endpoints.CREATE_ACCOUNT_ENDPOINT, json=payload)

    @staticmethod
    @allure.step('Отправка POST-запроса для авторизации пользователя')
    def login_user(payload):
        return requests.post(url=Endpoints.LOGIN_ACCOUNT_ENDPOINT, json=payload)

    @staticmethod
    @allure.step("Отправка DELETE-запроса для удаления пользователя")    
    def delete_user(token):
        return requests.delete(Endpoints.DELETE_ACCOUNT_ENDPOINT, headers={'Authorization': token})

    @staticmethod
    @allure.step("Отправка POST-запроса для создания заказа")
    def make_order(ingredients, token=None):
        payload = {'ingredients': ingredients}
        return requests.post(url=Endpoints.MAKE_ORDER_ENDPOINT, json=payload, headers={'Authorization': token})

    @staticmethod
    @allure.step("Отправка GET-запроса для получения данных об ингредиентах")
    def get_ingredients():
        return requests.get(url=Endpoints.GET_INGREDIENTS_INFO_ENDPOINT)
