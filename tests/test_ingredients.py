import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *

class TestIngridients:

    def test_get_price_ingridient(self):
        ingridient = Ingredient('SAUCE', 'cheese', 1.00)
        assert ingridient.get_price() == 1.00

    def test_get_name_ingridient(self):
        ingridient = Ingredient('SAUCE', 'cheese', 1.00)
        assert ingridient.get_name() == 'cheese'

    @pytest.mark.parametrize(
        'type, name, price, expected_ingredient',
        [
            [INGREDIENT_TYPE_SAUCE, 'Cheese', 1.00, 'SAUCE'],
            [INGREDIENT_TYPE_FILLING, 'Ketchup', 2.00, 'FILLING']
        ]
    )
    def test_get_type_ingridient(self, type, name, price, expected_ingredient):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == expected_ingredient