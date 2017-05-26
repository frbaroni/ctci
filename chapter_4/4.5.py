import unittest
from mytree import Tree

def checkBST(head):
    def check(node, minn, maxx):
        if node is None:
            return True
        if minn is not None:
            if node.value < minn:
                return False
        if maxx is not None:
            if node.value > maxx:
                return False
        return (
            check(node.left, minn, node.value)
            and
            check(node.right, node.value, maxx)
            )
    return check(head, None, None)
            

class Playground(unittest.TestCase):
    def test_valid_perfect(self):
        A = Tree.create_like([
            [      50      ],
            [  25,     75  ],
            [10, 40, 65, 80],
            ])
        self.assertTrue(checkBST(A))

    def test_valid_imperfect(self):
        A = Tree.create_like([
            [      50      ],
            [  25,     75  ],
            [10, 40, 65, None],
            ])
        self.assertTrue(checkBST(A))

    def test_invalid(self):
        A = Tree.create_like([
            [      50      ],
            [  25,     75  ],
            [10, 99, 65, 80],
            ])
        self.assertFalse(checkBST(A))


if __name__ == '__main__':
    unittest.main()
