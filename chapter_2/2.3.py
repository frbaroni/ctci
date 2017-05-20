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
        
def deleteElement(node):
    node.data = node.next.data
    node.next = node.next.next

class Playground(unittest.TestCase):
    def test_1(self):
        A = createLinkedList([1, 2, 3])
        E = [1, 3]
        deleteElement(A.next)
        self.assertEqual(toList(A), E)

    def test_1(self):
        A = createLinkedList([1, 2, 3])
        E = [2, 3]
        deleteElement(A)
        self.assertEqual(toList(A), E)

if __name__ == '__main__':
    unittest.main()
