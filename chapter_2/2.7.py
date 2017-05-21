import unittest
from mylist import LinkedList

def intersection(a, b):
    def size(head):
        s = 0
        n = head
        while n is not None:
            n = n.next
            s += 1
        return s
    def advance(node, k):
        n = node
        while k > 0:
            n = n.next
            k -= 1
        return n
    la = size(a)
    lb = size(b)
    na = a
    nb = b
    if la > lb:
        na = advance(na, la - lb)
    else:
        nb = advance(nb, lb - la)
    while na is not None:
        if na == nb:
            return na
        na = na.next
        nb = nb.next
    return None

class Playground(unittest.TestCase):
    def test_valid(self):
        A = LinkedList.create([1, 2, 3])
        B = LinkedList.create([2, 3])
        B.next.next = A
        E = B.next.next
        self.assertEqual(intersection(A, B), E)

    def test_invalid(self):
        A = LinkedList.create([1, 2, 3])
        B = LinkedList.create([2, 3, 1, 2])
        E = None
        self.assertEqual(intersection(A, B), E)

if __name__ == '__main__':
    unittest.main()
