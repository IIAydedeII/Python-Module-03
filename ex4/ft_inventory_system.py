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

    if not items:
        print(
            "No items provided. Usage: python3",
            sys.argv[0],
            "<item_name1>:<quantity> <item_name2>:<quantity> ...",
        )
        return

    item_list = list(items.keys())
    items_total = sum(items.values())
    print("Got inventory:", items)
    print("Item list:", item_list)
    print(f"Total quantity of the {len(item_list)} items:", items_total)

    extremes = {
        "most": ("", 0),
        "least": ("", 0),
    }

    first = True
    for item, amount in items.items():
        if first:
            extremes["most"] = extremes["least"] = (item, amount)
            first = False
        else:
            if amount > extremes["most"][1]:
                extremes["most"] = (item, amount)

            if amount < extremes["least"][1]:
                extremes["least"] = (item, amount)

        item_share = amount / items_total
        print(f"Item {item} represents {item_share:.1%}")

    print(
        "Item most abundant:",
        f"{extremes["most"][0]} with quantity {extremes["most"][1]}",
    )
    print(
        "Item least abundant:",
        f"{extremes["least"][0]} with quantity {extremes["least"][1]}",
    )

    items.update({"magic_item": 1})
    print("Updated inventory:", items)


if __name__ == "__main__":
    main()
