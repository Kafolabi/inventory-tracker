from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Item:
    """One stock item. The values are checked when the item is created."""

    item_name: str
    quantity: int
    price: float

    def __post_init__(self) -> None:
        if not self.item_name.strip():
            raise ValueError("item_name cannot be empty.")
        if self.quantity < 0:
            raise ValueError(f"{self.item_name}: quantity cannot be negative.")
        if self.price < 0:
            raise ValueError(f"{self.item_name}: price cannot be negative.")

    @property
    def value(self) -> float:
        """Stock value of this item: quantity x price."""
        return self.quantity * self.price


inventory: list[Item] = [
    Item("Laptop", 10, 450000),
    Item("Mouse", 50, 3500),
    Item("Keyboard", 30, 8000),
    Item("Monitor", 8, 120000),
    Item("USB Cable", 100, 1500),
    Item("Headset", 0, 15000),
]
