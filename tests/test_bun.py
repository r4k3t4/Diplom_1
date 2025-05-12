import pytest
from praktikum.bun import Bun

class TestBun:

    def test_add_new_ban(self):
        bun = Bun("mak", 3.75)
        assert bun.name == "mak" and bun.price == 3.75