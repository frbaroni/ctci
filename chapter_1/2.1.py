import unittest

class LinkedList:
    def __init__(s, value):
        s.data = value
        s.next = None

def createLinkedList(elements):
    res = None
    for element in reversed(elements):
        e = LinkedList(element)
        if res is not None:
            res.next = e
        res = e
    return res

def toList(linkedList):
    res = []
    n = linkedList
    while n is not None:
        res.append(n.data)
        n = n.next
    return res
        
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
            r.next = r.next
            p.next = p.next
        n = n.next
    return head


class Playground(unittest.TestCase):
    def test_nodups(self):
        A = createLinkedList([1, 2, 3])
        E = createLinkedList([1, 2, 3])
        self.assertEqual(toList(removeDupsSet(A)), toList(E))

    def test_hasdup(self):
        A = createLinkedList([1, 2, 1, 3])
        E = createLinkedList([1, 2, 3])
        self.assertEqual(toList(removeDupsSet(A)), toList(E))

    def test_lastisdup(self):
        A = createLinkedList([1, 2, 1, 3, 3])
        E = createLinkedList([1, 2, 3])
        self.assertEqual(toList(removeDupsSet(A)), toList(E))

    def test_firstisdup(self):
        A = createLinkedList([1, 1, 2, 1, 3])
        E = createLinkedList([1, 2, 3])
        self.assertEqual(toList(removeDupsSet(A)), toList(E))

    def test_2_nodups(self):
        A = createLinkedList([1, 2, 3])
        E = createLinkedList([1, 2, 3])
        self.assertEqual(toList(removeDups(A)), toList(E))

    def test_2_hasdup(self):
        A = createLinkedList([1, 2, 1, 3])
        E = createLinkedList([1, 2, 3])
        self.assertEqual(toList(removeDups(A)), toList(E))

    def test_2_lastisdup(self):
        A = createLinkedList([1, 2, 1, 3, 3])
        E = createLinkedList([1, 2, 3])
        self.assertEqual(toList(removeDups(A)), toList(E))

    def test_2_firstisdup(self):
        A = createLinkedList([1, 1, 2, 1, 3])
        E = createLinkedList([1, 2, 3])
        self.assertEqual(toList(removeDups(A)), toList(E))



if __name__ == '__main__':
    unittest.main()
