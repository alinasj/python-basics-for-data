"""05 — Scripts and argparse.

Notebooks are for exploring. A .py file is what you actually run from a terminal.

    python 05_argparse.py --name Fath --baths 5 --bedrooms 10 --kitchens 5

`if __name__ == "__main__"` means: run main() when this file is executed,
but not when another file imports House from it.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass
class House:
    name: str
    baths: int
    bedrooms: int
    kitchens: int

    def describe(self) -> str:
        return (
            f"{self.name}: {self.baths} baths, "
            f"{self.bedrooms} beds, {self.kitchens} kitchens"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Describe a house from CLI flags.")
    parser.add_argument("--name", required=True, help="owner name")
    parser.add_argument("--baths", type=int, required=True, help="number of bathrooms")
    parser.add_argument("--bedrooms", type=int, required=True, help="number of bedrooms")
    parser.add_argument("--kitchens", type=int, required=True, help="number of kitchens")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    house = House(args.name, args.baths, args.bedrooms, args.kitchens)
    print(house.describe())


if __name__ == "__main__":
    main()
