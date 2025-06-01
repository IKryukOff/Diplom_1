from praktikum.bun import Bun


class TestBun:
    def test_create_bun_name_is_correct(self) -> None:
        bun = Bun(name='Флюоресцентная булка R2-D3', price=988)
        assert bun.get_name() == 'Флюоресцентная булка R2-D3'

    def test_create_bun_price_is_correct(self) -> None:
        bun = Bun(name='Краторная булка N-200i', price=1255)
        assert bun.get_price() == 1255
