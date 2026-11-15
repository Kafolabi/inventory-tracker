from inventory import Item, inventory
from utils.helpers import highest_stock_item, lowest_stock_item, low_stock_items


def total_stock_value(items: list[Item]) -> float:
    total = 0
    for item in items:
        total = total + item.value
    return total


if __name__ == "__main__":
    print("Inventory Tracker")
    print("Items:", inventory)
    print("Total stock value:", total_stock_value(inventory))
    print("Highest stock item:", highest_stock_item(inventory))
    print("Lowest stock item:", lowest_stock_item(inventory))

    # New feature: low-stock alert
    print("Low stock (10 or fewer):", [item.item_name for item in low_stock_items(inventory)])

    # Checks
    print("Total value of an empty inventory:", total_stock_value([]))
    print("Highest stock item of an empty inventory:", highest_stock_item([]))
    try:
        Item("Printer", -5, 90000)
    except ValueError as error:
        print("Rejected:", error)
