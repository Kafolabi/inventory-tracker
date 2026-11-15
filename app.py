from inventory import inventory
from utils.helpers import highest_stock_item, lowest_stock_item


def total_stock_value(items):
    total = 0
    for item in items:
        # Bug fix: the value of an item is quantity x price.
        # The old code added only the price and ignored the quantity.
        total = total + item["quantity"] * item["price"]
    return total


# Bug fix: the output now runs only when app.py is executed directly
if __name__ == "__main__":
    print("Inventory Tracker")
    print("Items:", inventory)
    print("Total stock value:", total_stock_value(inventory))
    print("Highest stock item:", highest_stock_item(inventory))
    print("Lowest stock item:", lowest_stock_item(inventory))

    # Checks for the fixes
    print("Total value of an empty inventory:", total_stock_value([]))
    print("Highest stock item of an empty inventory:", highest_stock_item([]))
