import unittest
from mystack import Stack

class StackOfPlates(Stack):
    def __init__(self, max_elements=5):
        self.max_elements = max_elements
        super().__init__()

    def push(self, value):
        if super().size() == 0:
            super().push(Stack())
        last = super().peek()
        if last.size() >= self.max_elements:
            last = Stack()
            super().push(last)
        last.push(value)

    def pop(self):
        return self.popAt(super().size() - 1)

    def popAt(self, index):
        stack = self.data[index]
        value = stack.pop()
        if stack.size() == 0:
            self.data.remove(stack)
        return value

    def peek(self):
        stack = self.data[super().size() - 1]
        return stack.peek()

class Playground(unittest.TestCase):
    def test_stackofplates(self):
        s = StackOfPlates(2)
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        s.push(5)
        s.push(6)
        s.push(7)
        self.assertEqual(s.peek(), 7)
        self.assertEqual(s.pop(), 7)
        self.assertEqual(s.peek(), 6)
        self.assertEqual(s.pop(), 6)
        self.assertEqual(s.peek(), 5)
        self.assertEqual(s.popAt(1), 4)
        self.assertEqual(s.popAt(1), 3)
        self.assertEqual(s.popAt(1), 5)
        


if __name__ == '__main__':
    unittest.main()
