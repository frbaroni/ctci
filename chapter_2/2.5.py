import unittest
from mylist import LinkedList
        
def sumLists(a, b):
    head = LinkedList(None)
    out = head
    bit = 0
    while (a is not None) or (b is not None):
        va = a.data if a is not None else 0
        vb = b.data if b is not None else 0
        r = va + vb + bit
        bit = 1 if r > 9 else 0
        r %= 10
        out.next = LinkedList(r)
        out = out.next
        a = a.next
        b = b.next
    if bit:
        out.next = LinkedList(bit)
        out = out.next
    return head.next

class Playground(unittest.TestCase):
    def test_1(self):
        A = LinkedList.create([7, 1, 6])
        B = LinkedList.create([5, 9, 2])
        E = LinkedList.create([2, 1, 9])
        self.assertEqual(sumLists(A, B).toList(), E.toList())

if __name__ == '__main__':
    unittest.main()
