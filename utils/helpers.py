"""Calculations and formatting helpers for the Inventory Tracker.

Every function takes the list of items as an argument and returns a result
without printing or changing anything, so each one can be tested on its own.
"""

from inventory import REORDER_LEVEL, Item


# ---------------------------------------------------------------------------
# Totals
# ---------------------------------------------------------------------------

def total_stock_value(items: list[Item]) -> float:
    """Return the value of all stock: the sum of quantity x price."""
    return sum(item.value for item in items)


def total_units(items: list[Item]) -> int:
    """Return the number of units in stock across all items."""
    return sum(item.quantity for item in items)


# ---------------------------------------------------------------------------
# Finding items (each returns None for an empty list instead of failing)
# ---------------------------------------------------------------------------

def highest_stock_item(items: list[Item]) -> Item | None:
    """Return the item with the largest quantity."""
    return max(items, key=lambda item: item.quantity, default=None)


def lowest_stock_item(items: list[Item]) -> Item | None:
    """Return the item with the smallest quantity."""
    return min(items, key=lambda item: item.quantity, default=None)


def most_valuable_item(items: list[Item]) -> Item | None:
    """Return the item that holds the most money in stock."""
    return max(items, key=lambda item: item.value, default=None)


def low_stock_items(items: list[Item], reorder_level: int = REORDER_LEVEL) -> list[Item]:
    """Return the items at or below ``reorder_level``, including sold-out items."""
    return [item for item in items if item.quantity <= reorder_level]


# ---------------------------------------------------------------------------
# Formatting
# ---------------------------------------------------------------------------

def stock_status(item: Item, reorder_level: int = REORDER_LEVEL) -> str:
    """Return 'OUT', 'LOW' or 'OK' for an item."""
    if item.quantity == 0:
        return "OUT"
    if item.quantity <= reorder_level:
        return "LOW"
    return "OK"


def format_money(amount: float) -> str:
    """Format an amount in naira, for example 4500000 -> 'NGN 4,500,000.00'."""
    return f"NGN {amount:,.2f}"


def item_name_or_none(item: Item | None) -> str:
    """Return the item's name, or 'n/a' when there is no item."""
    return item.item_name if item is not None else "n/a"
