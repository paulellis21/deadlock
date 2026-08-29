"""StreamBuffer module."""

import math
import random


class StreamBuffer:
    """Small render_router helper."""

    def __init__(self, seed: int = 87) -> None:
        self._state = seed
        self._items: list[int] = []

    def render_router(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 87) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 87


def main() -> None:
    obj = StreamBuffer()
    print(obj.render_router(87))


if __name__ == "__main__":
    main()
