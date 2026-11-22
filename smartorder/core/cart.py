from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: float
    quantity: int = 1


class Cart:
    def __init__(self):
        self.items: list[Item] = []

    def add_product(self, name: str, price: float, quantity: int = 1) -> None:
        if price <= 0:
            raise ValueError("Cena produktu musi być większa od zera.")
        if quantity <= 0:
            raise ValueError("Ilość produktu musi być większa od zera.")

        for item in self.items:
            if item.name == name:
                item.quantity += quantity
                return

        self.items.append(Item(name=name, price=price, quantity=quantity))

    def remove_product(self, name: str) -> None:
        self.items = [item for item in self.items if item.name != name]

    def clear(self) -> None:
        self.items.clear()

    def get_total(self) -> float:
        return sum(item.price * item.quantity for item in self.items)
