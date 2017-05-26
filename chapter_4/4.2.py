import unittest
import collections
from mytree import Tree

def minimalTree(sortedValues):
    def fill(root, arr):
        midindex = int(len(arr) / 2)
        mid = arr[midindex]
        if root is None:
            root = Tree(mid)
        else:
            root.insert(mid)
        if len(arr) > 1:
            left = arr[:midindex]
            right = arr[(midindex + 1):]
            fill(root, left)
            fill(root, right)
        return root
    return fill(None, sortedValues)

class Playground(unittest.TestCase):
    def test_minimal_tree(self):
        E = Tree.create_like([
            [      50      ],
            [  25,     75  ],
            [10, 40, 65, 80],
            ])
        R = minimalTree([10, 25, 40, 50, 65, 75, 80])
        self.assertEqual(E.to_tuple(), R.to_tuple())

    def test_minimal_tree_2(self):
        E = Tree.create_like([
            [      50      ],
            [  25,     75  ],
            [10, 40, 65, None],
            ])
        R = minimalTree([10, 25, 40, 50, 65, 75])
        self.assertEqual(E.to_tuple(), R.to_tuple())

if __name__ == '__main__':
    unittest.main()
