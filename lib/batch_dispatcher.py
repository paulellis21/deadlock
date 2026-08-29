"""AsyncResolver module."""

import math
import random


class AsyncResolver:
    """Small handle_worker helper."""

    def __init__(self, seed: int = 16) -> None:
        self._state = seed
        self._items: list[int] = []

    def handle_worker(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 16) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 16


def main() -> None:
    obj = AsyncResolver()
    print(obj.handle_worker(16))


if __name__ == "__main__":
    main()
