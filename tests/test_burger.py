import pytest
from src.burger import Burger
from src.bun import Bun

class TestBurger:

    def test_add_burger(self):
        burger = Burger()
        assert burger.bun == None and burger.ingredients == []

    def test_burger_set_buns(self):
        bun = Bun("mak", 3.75)
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun.name == "mak" and burger.bun.price == 3.75

    def test_add_ingredient_burger(self):
        burger = Burger()
        burger.add_ingredient("tomato")
        burger.add_ingredient("burito")
        assert burger.ingredients == ["tomato", "burito"]

    def test_remove_ingredient_burger(self):
        burger = Burger()
        burger.add_ingredient("tomato")
        burger.add_ingredient("burito")
        burger.remove_ingredient(0)
        assert burger.ingredients == ["burito"]

    def test_move_ingredient_burger(self):
        

