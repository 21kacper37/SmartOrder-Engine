# Miejsce na fikstury testowe (@pytest.fixture)
import os
import tempfile
import pytest
from smartorder.core.cart import Cart, Item


@pytest.fixture
def empty_cart():
    return Cart()


@pytest.fixture
def sample_cart():
    cart = Cart()
    cart.add_product("Laptop", 3500.0, 1)
    cart.add_product("Myszka", 150.0, 2)
    cart.add_product("Klawiatura", 250.0, 1)
    return cart


@pytest.fixture
def temp_log_file():
    fd, path = tempfile.mkstemp(suffix=".log", prefix="smartorder_")
    os.close(fd)
    try:
        yield path
    finally:
        if os.path.exists(path):
            os.remove(path)
