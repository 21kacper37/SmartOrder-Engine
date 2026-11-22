# Miejsce na fikstury testowe (@pytest.fixture)
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
    return cart
