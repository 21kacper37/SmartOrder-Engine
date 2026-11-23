# Miejsce na testy parametryzowane rabatów (Część 2)
import pytest
from smartorder.core.discounts import calculate_discount, InvalidCouponError

# Uzupełnij testy z użyciem @pytest.mark.parametrize


@pytest.mark.parametrize(
    ("cart_total", "customer_tier", "promo_code", "expected_discount"),
    [
        (100.0, "REGULAR", None, 0.0),
        (100.0, "VIP", None, 0.10),
        (100.0, "PREMIUM", None, 0.15),
        (100.0, "REGULAR", "SUMMER2026", 0.10),
        (600.0, "VIP", "SUMMER2026", 0.25),
        (10000.0, "PREMIUM", "SUMMER2026", 0.50),
    ],
)
def test_calculate_discount_valid_combinations(
    cart_total, customer_tier, promo_code, expected_discount
):
    result = calculate_discount(
        cart_total=cart_total,
        customer_tier=customer_tier,
        promo_code=promo_code,
    )

    assert 0.0 <= result <= 0.50
    assert result == pytest.approx(expected_discount)


@pytest.mark.parametrize("invalid_coupon", ["WRONG2026", "EXPIRED", "", "   "])
def test_calculate_discount_invalid_coupon_raises_error(invalid_coupon):
    with pytest.raises(InvalidCouponError):
        calculate_discount(
            cart_total=100.0,
            customer_tier="REGULAR",
            promo_code=invalid_coupon,
        )


def test_calculate_discount_unknown_tier_raises_value_error():
    with pytest.raises(ValueError):
        calculate_discount(
            cart_total=100.0,
            customer_tier="UNKNOWN",
            promo_code=None,
        )


def test_calculate_discount_negative_cart_total_raises_value_error():
    with pytest.raises(ValueError):
        calculate_discount(
            cart_total=-1.0,
            customer_tier="REGULAR",
            promo_code=None,
        )
