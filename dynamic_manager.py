"""AsyncManager module."""

import math
import random


class AsyncManager:
    """Small decode_session helper."""

    def __init__(self, seed: int = 18) -> None:
        self._state = seed
        self._items: list[int] = []

    def decode_session(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 18) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 18


def main() -> None:
    obj = AsyncManager()
    print(obj.decode_session(18))


if __name__ == "__main__":
    main()
