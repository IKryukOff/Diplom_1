import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (INGREDIENT_TYPE_FILLING,
                                        INGREDIENT_TYPE_SAUCE)


class TestIngredient:
    def test_create_ingredient_name_is_correct(self) -> None:
        ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE,
                                name='Соус Spicy-X',
                                price=90)
        assert ingredient.get_name() == 'Соус Spicy-X'

    def test_create_ingredient_price_is_correct(self) -> None:
        ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING,
                                name='Говяжий метеорит (отбивная)',
                                price=3000)
        assert ingredient.get_price() == 3000

    @pytest.mark.parametrize(
            'ingredient_type,name,price,ingredient_type_value',
            [[INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90, 'SAUCE'],
             [INGREDIENT_TYPE_FILLING, 'Говяжий метеорит (отбивная)', 3000, 'FILLING']])
    def test_create_ingredient_type_is_correct(self,
                                               ingredient_type: str,
                                               name: str,
                                               price: int,
                                               ingredient_type_value: str) -> None:
        ingredient = Ingredient(ingredient_type=ingredient_type,
                                name=name,
                                price=price)
        assert ingredient.get_type() == ingredient_type_value
