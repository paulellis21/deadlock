"""LiteManager module."""

import math
import random


class LiteManager:
    """Small build_registry helper."""

    def __init__(self, seed: int = 65) -> None:
        self._state = seed
        self._items: list[int] = []

    def build_registry(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 65) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 65


def main() -> None:
    obj = LiteManager()
    print(obj.build_registry(65))


if __name__ == "__main__":
    main()
