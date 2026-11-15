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
    # New feature: items at or below the reorder level need restocking
    return [item for item in items if item.quantity <= reorder_level]
