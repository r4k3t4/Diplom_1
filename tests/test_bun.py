import pytest
from praktikum.bun import Bun

class TestBun:

    def test_get_name_bun(self):
        bun = Bun("mak", 3.75)
        assert bun.get_name() == "mak"

    def test_get_price_bun(self):
        bun = Bun("mak", 3.75)
        assert bun.get_price() == 3.75