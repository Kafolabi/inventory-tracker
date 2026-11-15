def highest_stock_item(items):
    return max(items, key=lambda item: item["quantity"])


def lowest_stock_item(items):
    return max(items, key=lambda item: item["price"])
