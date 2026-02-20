class Queue:
    def __init__(self, maxsize=-1):
        self.queue = []
        self.maxsize = maxsize

    def enqueue(self, item) -> None:
        if not self.is_full():
            self.queue.append(item)

    def dequeue(self) -> str:
        if not self.is_empty():
            return self.queue.pop(0)
        return ""

    def peek(self) -> str:
        if not self.is_empty():
            return self.queue[0]
        return ""

    def remove(self, item) -> None:
        if not self.is_empty():
            self.queue.remove(item)

    def is_empty(self) -> bool:
        return len(self.queue) <= 0

    def is_full(self) -> bool:
        return len(self.queue) == self.maxsize

    def size(self) -> int:
        return len(self.queue)

    def display(self) -> None:
        print(self.queue)

    def show(self):
        return self.queue


class PriorityQueue(Queue):
    def enqueue(self, item) -> None:
        if not self.is_full():
            self.queue.append(item)

        self.queue = sorted(self.queue, key=lambda x: x[1])

    def get(self, value):
        keys = [item[0] for item in self.queue]
        if value in keys:
            return self.queue[keys.index(value)]
        return None
