from inventory import Item


def highest_stock_item(items: list[Item]) -> Item | None:
    if not items:
        return None
    return max(items, key=lambda item: item.quantity)


def lowest_stock_item(items: list[Item]) -> Item | None:
    if not items:
        return None
    return min(items, key=lambda item: item.quantity)


def low_stock_items(items: list[Item], reorder_level: int = 10) -> list[Item]:
    # Items at or below the reorder level need restocking
    return [item for item in items if item.quantity <= reorder_level]


def most_valuable_item(items: list[Item]) -> Item | None:
    # Enhancement: the item that holds the most money in stock
    if not items:
        return None
    return max(items, key=lambda item: item.value)


def format_money(amount: float) -> str:
    # Enhancement: 4500000 -> "NGN 4,500,000.00"
    return f"NGN {amount:,.2f}"
