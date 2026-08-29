"""SimpleManager module."""

import math
import random


class SimpleManager:
    """Small collect_monitor helper."""

    def __init__(self, seed: int = 53) -> None:
        self._state = seed
        self._items: list[int] = []

    def collect_monitor(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 53) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 53


def main() -> None:
    obj = SimpleManager()
    print(obj.collect_monitor(53))


if __name__ == "__main__":
    main()
