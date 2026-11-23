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


def test_add_new_product_increases_item_count(empty_cart):
    #
    initial_count = len(empty_cart.items)

    
    empty_cart.add_product("Zeszyt", 15.0, 1)

    assert len(empty_cart.items) == initial_count + 1
    assert empty_cart.items[-1].name == "Zeszyt"


def test_add_duplicate_product_merges_and_sums_quantity(empty_cart):
    empty_cart.add_product("Książka", 50.0, 2)

    empty_cart.add_product("Książka", 50.0, 3)

    assert len(empty_cart.items) == 1
    assert empty_cart.items[0].name == "Książka"
    assert empty_cart.items[0].quantity == 5
    assert empty_cart.get_total() == 250.0


def test_add_product_zero_price_raises_value_error(empty_cart):
    with pytest.raises(ValueError):
        empty_cart.add_product("Darmowy produkt", 0.0, 1)


@pytest.mark.parametrize("invalid_quantity", [0, -1, -3])
def test_add_product_non_positive_quantity_raises_value_error(
    empty_cart, invalid_quantity
):
    with pytest.raises(ValueError):
        empty_cart.add_product("Książka", 50.0, invalid_quantity)


def test_remove_product_removes_item_from_cart(sample_cart):
    assert any(item.name == "Myszka" for item in sample_cart.items)

    sample_cart.remove_product("Myszka")

    assert all(item.name != "Myszka" for item in sample_cart.items)
    assert len(sample_cart.items) == 2


def test_clear_empties_cart_completely(sample_cart):
    assert len(sample_cart.items) > 0

    sample_cart.clear()

    assert len(sample_cart.items) == 0
    assert sample_cart.get_total() == 0.0


def test_get_total_returns_sum_of_price_times_quantity(sample_cart):
    expected_total = 4050.0

    total = sample_cart.get_total()

    assert total == pytest.approx(expected_total)
