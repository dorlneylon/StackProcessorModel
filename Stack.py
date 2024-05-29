class Stack:
    def __init__(self, max_size=10):
        self.stack = [0] * max_size
        self.max_size = max_size
        self.top = 0
    def __call_(self, operation, data = 0):
        if operation == 'push':
            if self.top < self.max_size:
                self.top += 1
            self.stack[self.top] = data
        if operation == 'pop':
            if self.top > 0:
                self.top -= 1
        if operation == 'peek':
            return self.stack[self.top]
        
def test_stack():
    stack = Stack()
    stack('push', 1)
    stack('push', 2)
    stack('push', 3)
    stack('push', 4)
    stack('push', 5)
    stack('push', 6)
    stack('push', 7)
    stack('push', 8)
    stack('push', 9)
    stack('push', 10)
    stack('push', 11)
    assert stack('peek') == 11
    stack('pop')
    assert stack('peek') == 10
    stack('pop')
   