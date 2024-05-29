import Stack
class StackHandler:
    def __init__(self, stack: Stack):
        self.stack = stack
    def push(self, value):
        self.stack("push", value)
    def pop(self):
        x = self.stack("peek")
        self.stack("pop")
        return x
    def top(self):
        return self.stack("peek")
    def dup(self):
        x = self.stack("peek")
        self.stack("push", x)
    def swap(self):
        x = self.stack("pop")
        y = self.stack("pop")
        self.stack("push", x)
        self.stack("push", y)

def test_stack_handler():
    stack = StackHandler(Stack())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.top() == 3
    assert stack.pop() == 3
    assert stack.pop() == 2

