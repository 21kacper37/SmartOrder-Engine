# Miejsce na testy jednostkowe koszyka (Część 1 & Część 3)
import pytest
from smartorder.core.cart import Cart

def test_add_product_increases_total(empty_cart):
    empty_cart.add_product("Książka", 50.0, 2)
    assert empty_cart.get_total() == 100.0

def test_add_product_invalid_price():
    cart = Cart()
    with pytest.raises(ValueError):
        cart.add_product("Błędny produkt", -10.0)
