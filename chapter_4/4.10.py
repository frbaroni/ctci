import unittest
from mytree import Tree

def isSubtree(a, b):
    def do(node, output):
        if node is None:
            output.append('(NULL)')
        else:
            output.append(node.value)
            do(node.left, output)
            do(node.right, output)
        return output

    def strize(head):
        return ",".join(map(str, do(head, [])))

    aa = strize(a)
    bb = strize(b)
    return aa.find(bb) != -1

class Playground(unittest.TestCase):
    def test_true(self):
        A = Tree.create_like([
            [      50      ],
            [  25,     75  ],
            [10, 40, 65, 80],
            ])
        B = Tree.create_like([
            [      75      ],
            [  65,     80  ]
            ])
        self.assertTrue(isSubtree(A, B))

    def test_false(self):
        A = Tree.create_like([
            [      50      ],
            [  25,     75  ],
            [10, 40, 65, 80],
            ])
        B = Tree.create_like([
            [      32      ],
            [  23,     44  ]
            ])
        self.assertFalse(isSubtree(A, B))

if __name__ == '__main__':
    unittest.main()
