"""Inventory Tracker - main script (release v1.0).

Run with:  python app.py   (Python 3.12 or newer)

Reads the items from inventory.py, calculates the total stock value and
prints a report. The calculations are in utils/helpers.py; this script only
decides what is shown and saved.
"""

import csv
from pathlib import Path

from inventory import Item, inventory
from utils.helpers import (
    format_money,
    highest_stock_item,
    item_name_or_none,
    low_stock_items,
    lowest_stock_item,
    most_valuable_item,
    stock_status,
    total_stock_value,
    total_units,
)

LINE = "=" * 66
REPORT_FILE = Path("stock_report.csv")


def print_table(items: list[Item]) -> None:
    """Print one aligned row per item with its stock value and status."""
    print(f" {'Item':<12} {'Qty':>5} {'Unit price':>18} {'Stock value':>20}  Status")
    print(f" {'-' * 12} {'-' * 5} {'-' * 18} {'-' * 20}  ------")
    for item in items:
        print(
            f" {item.item_name:<12} {item.quantity:>5} "
            f"{format_money(item.price):>18} {format_money(item.value):>20}  "
            f"{stock_status(item)}"
        )


def print_summary(items: list[Item]) -> None:
    """Print the totals and the items worth noticing."""
    restock = ", ".join(item.item_name for item in low_stock_items(items)) or "none"
    print()
    print(f" Total stock value : {format_money(total_stock_value(items))}")
    print(f" Total units       : {total_units(items)}")
    print(f" Highest stock     : {item_name_or_none(highest_stock_item(items))}")
    print(f" Lowest stock      : {item_name_or_none(lowest_stock_item(items))}")
    print(f" Most valuable     : {item_name_or_none(most_valuable_item(items))}")
    print(f" Needs restocking  : {restock}")


def save_report(items: list[Item], path: Path = REPORT_FILE) -> Path:
    """Write the inventory to a CSV file and return its path."""
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["item_name", "quantity", "price", "stock_value", "status"])
        for item in items:
            writer.writerow(
                [item.item_name, item.quantity, item.price, item.value, stock_status(item)]
            )
    return path


def main() -> None:
    """Print the report and save it to a CSV file."""
    print(LINE)
    print(" INVENTORY TRACKER  v1.0")
    print(LINE)
    print_table(inventory)
    print_summary(inventory)
    print(f" Report saved to   : {save_report(inventory)}")
    print(LINE)


if __name__ == "__main__":
    main()
