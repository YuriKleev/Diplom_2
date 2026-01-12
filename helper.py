import random
import string

def generate_random_ingredient_id(length):            # генератор хеша ингредиента
    letters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string
