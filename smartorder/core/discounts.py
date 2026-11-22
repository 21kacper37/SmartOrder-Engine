class InvalidCouponError(Exception):
    """Wyjątek rzucany w przypadku podania nieprawidłowego kodu rabatowego."""
    pass


def calculate_discount(cart_total: float, customer_tier: str, promo_code: str = None) -> float:
    if cart_total < 0:
        raise ValueError("Wartość koszyka nie może być ujemna.")

    discount = 0.0
    tier = customer_tier.upper() if customer_tier else "REGULAR"

    if tier == "VIP":
        discount += 0.10
    elif tier == "PREMIUM":
        discount += 0.15
    elif tier != "REGULAR":
        raise ValueError(f"Nieznany poziom klienta: {customer_tier}")

    if promo_code is not None:
        if promo_code == "SUMMER2026":
            discount += 0.10
        else:
            raise InvalidCouponError("Nieprawidłowy kod promocyjny.")

    if cart_total > 500:
        discount += 0.05

    return min(discount, 0.50)  # Maksymalny możliwy rabat wynosi 50%
