#class for stack data-strcuture

class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, item) -> None:
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()
    
    def isEmpty(self) -> bool:
        return len(self.stack) == 0
    
    def peek(self):
        return self.stack[len(self.stack) - 1]

    def display(self):
        print(self.stack)

    def clearAll(self):
        self.stack.clear()
