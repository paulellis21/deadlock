"""RemoteRegistry module."""

import math
import random


class RemoteRegistry:
    """Small handle_session helper."""

    def __init__(self, seed: int = 47) -> None:
        self._state = seed
        self._items: list[int] = []

    def handle_session(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 47) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 47


def main() -> None:
    obj = RemoteRegistry()
    print(obj.handle_session(47))


if __name__ == "__main__":
    main()
