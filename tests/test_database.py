from praktikum.database import Database


class TestDatabase:
    def test_create_database_available_buns_len_is_correct(self) -> None:
        database = Database()
        assert len(database.available_buns()) == 3

    def test_create_database_available_ingredients_len_is_correct(self) -> None:
        database = Database()
        assert len(database.available_ingredients()) == 6
