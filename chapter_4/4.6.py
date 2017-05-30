import unittest
from mytree import Tree

def treeSucessor(node):
    def leftMost(n):
        l = n
        while l.left is not None:
            l = l.left
        return l
    if node is None:
        return None
    if node.right is not None:
        return leftMost(node.right)
    p = node
    while p.parent is not None:
        if p.parent.left == p:
            return p.parent
        p = p.parent
    return None
            

class Playground(unittest.TestCase):
    def setUp(self):
        self.A = Tree.create_like([
            [      50      ],
            [  25,     75  ],
            [10, 40, 65, 80],
            ])

    def test_sucessor_1(self):
        A = self.A
        N = A.findByValue(25)
        E = A.findByValue(40)
        self.assertEqual(treeSucessor(N).value, E.value)

    def test_sucessor_2(self):
        A = self.A
        N = A.findByValue(10)
        E = A.findByValue(25)
        self.assertEqual(treeSucessor(N).value, E.value)

    def test_sucessor_3(self):
        A = self.A
        N = A.findByValue(50)
        E = A.findByValue(65)
        self.assertEqual(treeSucessor(N).value, E.value)

    def test_sucessor_4(self):
        A = self.A
        N = A.findByValue(40)
        E = A.findByValue(50)
        self.assertEqual(treeSucessor(N).value, E.value)

    def test_sucessor_5(self):
        A = self.A
        N = A.findByValue(75)
        E = A.findByValue(80)
        self.assertEqual(treeSucessor(N).value, E.value)

    def test_last(self):
        A = self.A
        N = A.findByValue(80)
        E = None
        self.assertEqual(treeSucessor(N), E)


if __name__ == '__main__':
    unittest.main()
