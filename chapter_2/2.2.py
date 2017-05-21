import unittest
from mylist import LinkedList

def toList(linkedList):
    return linkedlist.toList()
        
def kthToLast(head, k):
    n = head
    r = head
    for i in range(k):
        if r is None:
            return None
        r = r.next
    while r is not None:
        r = r.next
        n = n.next
    return n.data

class Playground(unittest.TestCase):
    def test_1(self):
        A = [1, 2, 3]
        K = 1
        E = 3
        self.assertEqual(kthToLast(LinkedList.create(A), K), E)

    def test_2(self):
        A = [1, 2, 3]
        K = 2
        E = 2
        self.assertEqual(kthToLast(LinkedList.create(A), K), E)

    def test_3(self):
        A = [1, 2, 3]
        K = 3
        E = 1
        self.assertEqual(kthToLast(LinkedList.create(A), K), E)

    def test_4(self):
        A = [1, 2, 3]
        K = 4
        E = None
        self.assertEqual(kthToLast(LinkedList.create(A), K), E)


if __name__ == '__main__':
    unittest.main()
