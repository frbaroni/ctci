import unittest
from mylist import LinkedList
        
def partition(head, P):
    n = head
    while n is not None:
        if n.data >= P:
            s = n.next
            while s is not None:
                if s.data < P:
                    tmp = n.data
                    n.data = s.data
                    s.data = tmp
                    break
                s = s.next
            if s is None:
                break
        n = n.next
    return head

class Playground(unittest.TestCase):
    def test_1(self):
        A = [3, 5, 8, 5, 10, 2, 1]
        P = 5
        E = [3, 2, 1, 5, 10, 5, 8]
        self.assertEqual(partition(LinkedList.create(A), P).toList(), E)

if __name__ == '__main__':
    unittest.main()
