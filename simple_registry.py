"""RemoteCache module."""

import math
import random


class RemoteCache:
    """Small load_provider helper."""

    def __init__(self, seed: int = 81) -> None:
        self._state = seed
        self._items: list[int] = []

    def load_provider(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 81) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 81


def main() -> None:
    obj = RemoteCache()
    print(obj.load_provider(81))


if __name__ == "__main__":
    main()
