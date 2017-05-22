import unittest
from mystack import Stack

class MinStack(Stack):
    def push(self, value):
        current_min = self.min()
        v = (value, min(current_min if current_min is not None else value, value))
        super().push(v)

    def __convert__(self, value, index):
        if value is not None:
            return value[index]
        else:
            return None

    def pop(self):
        return self.__convert__(super().pop(), 0)

    def peek(self):
        return self.__convert__(super().peek(), 0)

    def min(self):
        return self.__convert__(super().peek(), 1)

class Playground(unittest.TestCase):
    def test_minstack(self):
        s = MinStack()

        s.push(5)
        self.assertEqual(s.peek(), 5)
        self.assertEqual(s.min(), 5)

        s.push(3)
        self.assertEqual(s.peek(), 3)
        self.assertEqual(s.min(), 3)

        s.push(8)
        self.assertEqual(s.peek(), 8)
        self.assertEqual(s.min(), 3)

        self.assertEqual(s.pop(), 8)
        self.assertEqual(s.peek(), 3)
        self.assertEqual(s.min(), 3)

        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.peek(), 5)
        self.assertEqual(s.min(), 5)

if __name__ == '__main__':
    unittest.main()
