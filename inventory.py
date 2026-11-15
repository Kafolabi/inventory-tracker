"""Inventory data for the Inventory Tracker.

This module holds the ``Item`` record and the list of items in stock.
It contains data only: every calculation lives in utils/helpers.py.
"""

from dataclasses import dataclass

# Items with this quantity or less are flagged for restocking.
REORDER_LEVEL = 10


@dataclass(frozen=True, slots=True)
class Item:
    """One stock item.

    The record is frozen, so an item cannot be changed by accident after it
    is created, and the values are validated in ``__post_init__``.

    Attributes:
        item_name: Name of the item. Must not be empty.
        quantity: Units in stock. Must be 0 or more.
        price: Price of one unit in naira. Must be 0 or more.
    """

    item_name: str
    quantity: int
    price: float

    def __post_init__(self) -> None:
        """Reject values that would make the stock figures meaningless."""
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
