import unittest
from mytree import Tree

def firstCommonAncestor(a, b):
    def up(node, parents, common):
        if not node:
            return (False, None)
        if node in common:
            return (True, node)
        parents.add(node)
        return (False, node.parent)
    pAs = set()
    pBs = set()
    pA = a
    pB = b
    while pA or pB:
        (ok, pA) = up(pA, pAs, pBs)
        if ok: return pA
        (ok, pB) = up(pB, pBs, pAs)
        if ok: return pB
    return None
            

class Playground(unittest.TestCase):
    def setUp(self):
        self.T = Tree.create_like([
            [      50      ],
            [  25,     75  ],
            [10, 40, 65, 80],
            ])

    def test_ancestor_1(self):
        T = self.T
        A = T.findByValue(10)
        B = T.findByValue(65)
        FCA = T.findByValue(50)
        self.assertEqual(firstCommonAncestor(A, B), FCA)

    def test_ancestor_2(self):
        T = self.T
        A = T.findByValue(10)
        B = T.findByValue(40)
        FCA = T.findByValue(25)
        self.assertEqual(firstCommonAncestor(A, B), FCA)

    def test_ancestor_3(self):
        T = self.T
        A = T.findByValue(40)
        B = T.findByValue(75)
        FCA = T.findByValue(50)
        self.assertEqual(firstCommonAncestor(A, B), FCA)

    def test_ancestor_4(self):
        T = self.T
        A = T.findByValue(80)
        B = T.findByValue(25)
        FCA = T.findByValue(50)
        self.assertEqual(firstCommonAncestor(A, B), FCA)


if __name__ == '__main__':
    unittest.main()
