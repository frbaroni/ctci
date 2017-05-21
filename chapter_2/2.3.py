import unittest
from mylist import LinkedList
        
def deleteElement(node):
    node.data = node.next.data
    node.next = node.next.next

class Playground(unittest.TestCase):
    def test_1(self):
        A = LinkedList.create([1, 2, 3])
        E = [1, 3]
        deleteElement(A.next)
        self.assertEqual(A.toList(), E)

    def test_1(self):
        A = LinkedList.create([1, 2, 3])
        E = [2, 3]
        deleteElement(A)
        self.assertEqual(A.toList(), E)

if __name__ == '__main__':
    unittest.main()
