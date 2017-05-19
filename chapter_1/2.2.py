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
            e.next = res
        res = e
    return res

def toList(linkedList):
    res = []
    n = linkedList
    while n is not None:
        res.append(n.data)
        n = n.next
    return res
        
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
        self.assertEqual(kthToLast(createLinkedList(A), K), E)

    def test_2(self):
        A = [1, 2, 3]
        K = 2
        E = 2
        self.assertEqual(kthToLast(createLinkedList(A), K), E)

    def test_3(self):
        A = [1, 2, 3]
        K = 3
        E = 1
        self.assertEqual(kthToLast(createLinkedList(A), K), E)

    def test_4(self):
        A = [1, 2, 3]
        K = 4
        E = None
        self.assertEqual(kthToLast(createLinkedList(A), K), E)


if __name__ == '__main__':
    unittest.main()
