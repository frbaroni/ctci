import unittest
from mytree import Tree

def calcDepth(head):
    def calc(node, level):
        if node is None:
            return level
        return max(
                calc(node.left, level + 1),
                calc(node.right, level + 1)
                )
    return calc(head, 0)

def isBalanced(head):
    if head is None:
        return False
    left = calcDepth(head.left)
    right = calcDepth(head.right)
    return abs(left - right) <= 1

class Playground(unittest.TestCase):
    def test_balanced(self):
        A = Tree.create_like([
            [      50      ],
            [  25,     75  ],
            [10, 40, 65, 80],
            ])
        self.assertTrue(isBalanced(A))

    def test_balanced_1(self):
        A = Tree.create_like([
            [      50      ],
            [  25,     75  ],
            [10, None, 65, None],
            ])
        self.assertTrue(isBalanced(A))

    def test_unbalanced(self):
        A = Tree.create_like([
            [      50      ],
            [  25,     None  ],
            [10, None, None, None],
            ])
        self.assertFalse(isBalanced(A))

if __name__ == '__main__':
    unittest.main()
