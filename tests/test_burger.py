from unittest.mock import Mock

from praktikum.burger import Burger


class TestBurger:
    def test_set_bun_in_burger_bun_is_correct(self) -> None:
        burger = Burger()
        bun = Mock()
        burger.set_buns(bun=bun)
        assert burger.bun == bun

    def test_add_ingredient_in_burger_list_of_ingredients_is_correct(self) -> None:
        burger = Burger()
        ingredient = Mock()
        len_of_ingredients_before = len(burger.ingredients)
        burger.add_ingredient(ingredient=ingredient)
        assert (ingredient in burger.ingredients and
                len(burger.ingredients) > len_of_ingredients_before)

    def test_remove_ingredient_from_burger_list_of_ingredients_is_correct(self) -> None:
        burger = Burger()
        ingredient = Mock()
        burger.add_ingredient(ingredient=ingredient)
        len_of_ingredients_before = len(burger.ingredients)
        burger.remove_ingredient(0)
        assert (ingredient not in burger.ingredients and
                len(burger.ingredients) < len_of_ingredients_before)

    def test_move_ingredient_new_place_of_ingredient_is_correct(self) -> None:
        burger = Burger()
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        before_moving_ingredient_i_is_first = burger.ingredients[0] == ingredient_1
        burger.move_ingredient(0, 1)
        assert (before_moving_ingredient_i_is_first is True and
                burger.ingredients[0] == ingredient_2 and
                burger.ingredients[1] == ingredient_1)

    def test_get_prace_of_burger_price_is_correct(self) -> None:
        burger = Burger()
        bun = Mock()
        ingredient = Mock()
        bun.get_price.return_value = 1255
        ingredient.get_price.return_value = 90
        burger.set_buns(bun=bun)
        burger.add_ingredient(ingredient=ingredient)
        assert burger.get_price() == 2600

    def test_get_receipt_of_burger_output_is_correct(self) -> None:
        burger = Burger()
        bun = Mock()
        ingredient = Mock()
        bun.get_name.return_value = 'Краторная булка N-200i'
        bun.get_price.return_value = 1255
        ingredient.get_name.return_value = 'Соус Spicy-X'
        ingredient.get_price.return_value = 90
        ingredient.get_type.return_value = 'SAUCE'
        burger.set_buns(bun=bun)
        burger.add_ingredient(ingredient=ingredient)
        assert burger.get_receipt() == \
'''(==== Краторная булка N-200i ====)
= sauce Соус Spicy-X =
(==== Краторная булка N-200i ====)

Price: 2600'''
