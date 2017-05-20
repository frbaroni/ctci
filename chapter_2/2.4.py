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
        self.assertEqual(toList(partition(createLinkedList(A), P)), E)

if __name__ == '__main__':
    unittest.main()
