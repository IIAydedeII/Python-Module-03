#!/usr/bin/env python3
import sys


class RedundantItemError(ValueError):
    """Raised when an item is specified more than once."""


def main() -> None:
    print("=== Inventory System Analysis ===")

    args = sys.argv[1:]
    items = {}

    for arg in args:
        try:
            item_name, quantity = arg.split(":")
            if item_name in items:
                raise RedundantItemError
        except RedundantItemError:
            print(f"Redundant item '{item_name}' - discarding")
            continue
        except ValueError:
            print(f"Error - invalid parameter '{arg}'")
            continue

        try:
            items[item_name] = int(quantity)
        except ValueError as e:
            print(f"Quantity error for '{item_name}':", e)

    print("Got inventory:", items)

    if items:
        item_list = list(items.keys())
        items_total = sum(items.values())
        print("Item list:", item_list)
        print(f"Total quantity of the {len(item_list)} items:", items_total)

        most_item = least_item = None
        most_amount = least_amount = 0

        for item, amount in items.items():
            if most_item is None:
                most_item = least_item = item
                most_amount = least_amount = amount

            if amount > most_amount:
                most_item = item
                most_amount = amount

            if amount < least_amount:
                least_item = item
                least_amount = amount

            item_share = amount / items_total
            print(f"Item {item} represents {item_share:.1%}")

        print(
            f"Item most abundant: {most_item}",
            f"with quantity {most_amount}",
        )
        print(
            f"Item least abundant: {least_item}",
            f"with quantity {least_amount}",
        )

    items.update({"magic_item": 1})
    print("Updated inventory:", items)


if __name__ == "__main__":
    main()
