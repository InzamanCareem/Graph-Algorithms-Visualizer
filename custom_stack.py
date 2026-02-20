class Stack:
    def __init__(self, maxsize=-1):
        self.stack = []
        self.maxsize = maxsize

    def push(self, item: str) -> None:
        if not self.is_full():
            self.stack.append(item)

    def pop(self) -> str:
        if not self.is_empty():
            return self.stack.pop()
        return ""

    def peek(self) -> str:
        if not self.is_empty():
            return self.stack[len(self.stack) - 1]
        return ""

    def is_empty(self) -> bool:
        return len(self.stack) <= 0

    def is_full(self) -> bool:
        return len(self.stack) == self.maxsize

    def size(self) -> int:
        return len(self.stack)

    def display(self) -> None:
        print(self.stack)

    def show(self):
        return self.stack
