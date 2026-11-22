def print_receipt(cart_items: list[dict], total: float) -> None:
    """
    Wypisuje sformatowany paragon na standardowe wyjście (sys.stdout).
    """
    print("=== PARAGON ===")
    for item in cart_items:
        name = item.get("name", "Produkt")
        price = item.get("price", 0.0)
        qty = item.get("quantity", 1)
        print(f"- {name} x{qty}: {price * qty:.2f} PLN")
    print(f"SUMA: {total:.2f} PLN")
    print("===============")


def confirm_order_cli() -> bool:
    """
    Pobiera odpowiedź od użytkownika ze standardowego wejścia (input).
    """
    response = input("Czy chcesz sfinalizować zamówienie? (Y/N): ")
    return response.strip().upper() == "Y"
