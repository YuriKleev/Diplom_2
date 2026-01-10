import pytest

import random

from faker import Faker

from data import TestData
from methods import Methods


@pytest.fixture(scope="function")
def new_user_data():

    faker = Faker()
    email = 'yuri_kleev_35_'+str(random.randint(100,9999))+'@ya.ru'
    password = faker.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
    name = faker.first_name()
    user_data = {
        'email': email,
        'password': password,
        'name': name
    }
    return user_data


@pytest.fixture(scope="function")
def user_with_valid_data():
    user_data = TestData.USER_DATA.copy()
    return user_data


@pytest.fixture(scope="function")
def ingredients():
    response = Methods.get_ingredients()
    return response.json()['data']
