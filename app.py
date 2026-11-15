import csv

from inventory import Item, inventory
from utils.helpers import (
    highest_stock_item,
    lowest_stock_item,
    low_stock_items,
    most_valuable_item,
    format_money,
)


def total_stock_value(items: list[Item]) -> float:
    total = 0
    for item in items:
        total = total + item.value
    return total


if __name__ == "__main__":
    line = "=" * 66
    print(line)
    print(" INVENTORY TRACKER")
    print(line)

    # Enhancement: aligned table with the value of every item
    print(f" {'Item':<12} {'Qty':>5} {'Unit price':>18} {'Stock value':>20}  Status")
    print(f" {'-' * 12} {'-' * 5} {'-' * 18} {'-' * 20}  ------")
    for item in inventory:
        if item.quantity == 0:
            status = "OUT"
        elif item.quantity <= 10:
            status = "LOW"
        else:
            status = "OK"
        print(f" {item.item_name:<12} {item.quantity:>5} {format_money(item.price):>18} {format_money(item.value):>20}  {status}")

    print()
    print(f" Total stock value : {format_money(total_stock_value(inventory))}")
    print(f" Total units       : {sum(item.quantity for item in inventory)}")
    print(f" Highest stock     : {highest_stock_item(inventory).item_name}")
    print(f" Lowest stock      : {lowest_stock_item(inventory).item_name}")
    print(f" Most valuable     : {most_valuable_item(inventory).item_name}")
    print(f" Needs restocking  : {', '.join(item.item_name for item in low_stock_items(inventory))}")

    # Enhancement: save the report so it can be opened in Excel
    with open("stock_report.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["item_name", "quantity", "price", "stock_value"])
        for item in inventory:
            writer.writerow([item.item_name, item.quantity, item.price, item.value])
    print(" Report saved to   : stock_report.csv")
    print(line)
