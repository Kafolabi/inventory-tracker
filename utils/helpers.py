def highest_stock_item(items):
    # Bug fix: max() raises ValueError on an empty list
    if not items:
        return None
    return max(items, key=lambda item: item["quantity"])


def lowest_stock_item(items):
    if not items:
        return None
    # Bug fix: this used max() on the price, so it returned the most
    # expensive item instead of the item with the lowest quantity
    return min(items, key=lambda item: item["quantity"])
