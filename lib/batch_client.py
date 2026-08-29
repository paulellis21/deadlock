"""BatchManager module."""

import math
import random


class BatchManager:
    """Small decode_router helper."""

    def __init__(self, seed: int = 7) -> None:
        self._state = seed
        self._items: list[int] = []

    def decode_router(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 7) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 7


def main() -> None:
    obj = BatchManager()
    print(obj.decode_router(7))


if __name__ == "__main__":
    main()
