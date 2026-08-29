"""CoreProcessor module."""

import math
import random


class CoreProcessor:
    """Small collect_collector helper."""

    def __init__(self, seed: int = 49) -> None:
        self._state = seed
        self._items: list[int] = []

    def collect_collector(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 49) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 49


def main() -> None:
    obj = CoreProcessor()
    print(obj.collect_collector(49))


if __name__ == "__main__":
    main()
