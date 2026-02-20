from typing import List, TypeVar, Tuple

T = TypeVar('T')

class Queue:
    def __init__(self, maxsize=-1):
        self.queue = []
        self.maxsize = maxsize

    def enqueue(self, item: T) -> None:
        if not self.is_full():
            self.queue.append(item)

    def dequeue(self) -> T:
        if not self.is_empty():
            return self.queue.pop(0)
        return ""

    def peek(self) -> T:
        if not self.is_empty():
            return self.queue[0]
        return ""

    def remove(self, item: T) -> None:
        if self.is_empty():
            raise IndexError("Cannot remove from empty queue")

        if item not in self.queue:
            raise ValueError(f"Item: {item} not in the queue")

        self.queue.remove(item)

    def is_empty(self) -> bool:
        return len(self.queue) <= 0

    def is_full(self) -> bool:
        return len(self.queue) == self.maxsize

    def size(self) -> int:
        return len(self.queue)

    def display(self) -> None:
        print(self.queue)

    def show(self) -> List[T]:
        return self.queue


class PriorityQueue(Queue):
    def enqueue(self, item: Tuple[T, int]) -> None:
        if not self.is_full():
            self.queue.append(item)

        self.queue = sorted(self.queue, key=lambda x: x[1])

    def get(self, value: int):
        keys = [item[0] for item in self.queue]
        if value in keys:
            return self.queue[keys.index(value)]
        return None
