import unittest
from mystack import Stack

class TwoStacksOneQueue:
    def __init__(self):
        self.back = Stack()
        self.front = Stack()

    def push(self, value):
        self.back.push(value)

    def peek(self):
        if self.front.size() == 0:
            while self.back.size() > 0:
                self.front.push(self.back.pop())
        return self.front.peek()

    def pop(self):
        value = self.peek()
        self.front.pop()
        return value


class Playground(unittest.TestCase):
    def test_queue(self):
        s = TwoStacksOneQueue()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.peek(), 2)
        self.assertEqual(s.pop(), 2)
        s.push(5)
        s.push(6)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 4)
        self.assertEqual(s.pop(), 5)
        self.assertEqual(s.pop(), 6)

if __name__ == '__main__':
    unittest.main()
