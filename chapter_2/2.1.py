import unittest
from mylist import LinkedList
        
# Using set() to hold known elements
def removeDupsSet(head):
    found = set()
    n = head
    while n is not None:
        found.add(n.data)
        if n.next is not None:
            if n.next.data in found:
                n.next = n.next.next
        n = n.next
    return head

# Not storing known elements
def removeDups(head):
    n = head
    while n is not None:
        r = n.next
        p = n
        while r is not None:
            if n.data == r.data:
                p.next = r.next
            else:
                p = p.next
            r = r.next
        n = n.next
    return head

def toList(l):
    return l.toList()

class Playground(unittest.TestCase):
    def test_nodups(self):
        A = LinkedList.create([1, 2, 3])
        E = LinkedList.create([1, 2, 3])
        self.assertEqual(toList(removeDupsSet(A)), toList(E))

    def test_hasdup(self):
        A = LinkedList.create([1, 2, 1, 3])
        E = LinkedList.create([1, 2, 3])
        self.assertEqual(toList(removeDupsSet(A)), toList(E))

    def test_lastisdup(self):
        A = LinkedList.create([1, 2, 1, 3, 3])
        E = LinkedList.create([1, 2, 3])
        self.assertEqual(toList(removeDupsSet(A)), toList(E))

    def test_firstisdup(self):
        A = LinkedList.create([1, 1, 2, 1, 3])
        E = LinkedList.create([1, 2, 3])
        self.assertEqual(toList(removeDupsSet(A)), toList(E))

    def test_2_nodups(self):
        A = LinkedList.create([1, 2, 3])
        E = LinkedList.create([1, 2, 3])
        self.assertEqual(toList(removeDups(A)), toList(E))

    def test_2_hasdup(self):
        A = LinkedList.create([1, 2, 1, 3])
        E = LinkedList.create([1, 2, 3])
        self.assertEqual(toList(removeDups(A)), toList(E))

    def test_2_lastisdup(self):
        A = LinkedList.create([1, 2, 1, 3, 3])
        E = LinkedList.create([1, 2, 3])
        self.assertEqual(toList(removeDups(A)), toList(E))

    def test_2_firstisdup(self):
        A = LinkedList.create([1, 1, 2, 1, 3])
        E = LinkedList.create([1, 2, 3])
        self.assertEqual(toList(removeDups(A)), toList(E))



if __name__ == '__main__':
    unittest.main()
