from inventory import inventory
from utils.helpers import highest_stock_item, lowest_stock_item


def total_stock_value(items):
    total = 0
    for item in items:
        total = total + item["price"]
    return total


print("Inventory Tracker")
print("Items:", inventory)
print("Total stock value:", total_stock_value(inventory))
print("Highest stock item:", highest_stock_item(inventory))
print("Lowest stock item:", lowest_stock_item(inventory))
