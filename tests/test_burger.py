import pytest
from praktikum.burger import Burger
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
import praktikum.ingredient_types

class TestBurger:

    def test_set_buns(self):
        bun = Bun("mak", 3.75)
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_burger(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'tomato'
        mock_ingredient.get_price.return_value = 6.00
        mock_ingredient.get_type.return_value = praktikum.ingredient_types.INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].get_price() == 6.00
        assert burger.ingredients[0].get_name() == 'tomato'
        assert burger.ingredients[0].get_type() == praktikum.ingredient_types.INGREDIENT_TYPE_FILLING

    def test_remove_ingredient_burger(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient_burger(self):
        burger = Burger()
        burger.add_ingredient("tomato")
        burger.add_ingredient("burito")
        burger.move_ingredient(0, 1)
        assert burger.ingredients == ["burito", "tomato"]

    def test_get_burger_price(self):
        burger = Burger()
        cheese = Ingredient('products', 'cheese', 1.00)
        burger.ingredients.append(cheese)
        burger.bun = Bun("mak", 3.00)
        assert burger.get_price() == 7.00

    def test_get_burger_receipt(self):
        burger = Burger()
        cheese = Ingredient('products', 'cheese', 1.00)
        burger.ingredients.append(cheese)
        burger.bun = Bun("mak", 3.00)
        assert burger.get_receipt() == f'(==== {burger.bun.get_name()} ====)\n= {cheese.get_type()} {cheese.get_name()} =\n(==== {burger.bun.name} ====)\n\nPrice: {burger.get_price()}'



