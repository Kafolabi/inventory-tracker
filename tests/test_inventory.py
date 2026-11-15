"""Unit tests for the Inventory Tracker.

Run from the project folder with:  python -m unittest -v
"""

import unittest

from inventory import Item
from utils.helpers import (
    format_money,
    highest_stock_item,
    low_stock_items,
    lowest_stock_item,
    most_valuable_item,
    stock_status,
    total_stock_value,
    total_units,
)

ITEMS = [
    Item("Laptop", 2, 500000),
    Item("Mouse", 50, 3000),
    Item("Headset", 0, 15000),
]


class TotalTests(unittest.TestCase):
    def test_total_value_multiplies_quantity_by_price(self):
        # 2 x 500000 + 50 x 3000 + 0 x 15000
        self.assertEqual(total_stock_value(ITEMS), 1_150_000)

    def test_total_units(self):
        self.assertEqual(total_units(ITEMS), 52)

    def test_empty_inventory(self):
        self.assertEqual(total_stock_value([]), 0)
        self.assertEqual(total_units([]), 0)
        self.assertIsNone(highest_stock_item([]))
        self.assertIsNone(lowest_stock_item([]))
        self.assertIsNone(most_valuable_item([]))
        self.assertEqual(low_stock_items([]), [])


class FindingTests(unittest.TestCase):
    def test_highest_and_lowest_use_quantity(self):
        self.assertEqual(highest_stock_item(ITEMS).item_name, "Mouse")
        self.assertEqual(lowest_stock_item(ITEMS).item_name, "Headset")

    def test_most_valuable_uses_stock_value(self):
        self.assertEqual(most_valuable_item(ITEMS).item_name, "Laptop")

    def test_low_stock_and_status(self):
        names = [item.item_name for item in low_stock_items(ITEMS)]
        self.assertEqual(names, ["Laptop", "Headset"])
        self.assertEqual([stock_status(item) for item in ITEMS], ["LOW", "OK", "OUT"])


class ItemTests(unittest.TestCase):
    def test_invalid_items_are_rejected(self):
        for args in [("", 1, 100), ("Printer", -5, 100), ("Printer", 5, -100)]:
            with self.assertRaises(ValueError):
                Item(*args)

    def test_format_money(self):
        self.assertEqual(format_money(4500000), "NGN 4,500,000.00")


if __name__ == "__main__":
    unittest.main()
