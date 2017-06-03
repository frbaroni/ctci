import unittest
from mytree import Tree

def countSumTo(head, sumTo):
    def sub(node, current_sum, total_sum):
        if node:
            value = current_sum + node.value
            if value == sumTo:
                total_sum += 1
            total_sum = sub(node.left, value, total_sum)
            total_sum = sub(node.right, value, total_sum)
            if head != node:
                total_sub_sum = countSumTo(node, sumTo)
                total_sum += total_sub_sum
        return total_sum

    return sub(head, 0, 0)

class Playground(unittest.TestCase):
    def setUp(self):
        self.A = Tree.create_like([
                [     5    ],
                [  2,   7  ],
                [1, 3, 6, 8],
                ])
        self.B = Tree.create_like([
                [                  10                  ],
                [       5,                  -3         ],
                [  3,       2,      None,        11    ],
                [3, -2, None, 1, None, None, None, None]
                ])

    def test_A5(self):
        self.assertEqual(countSumTo(self.A, 5), 2)

    def test_A7(self):
        self.assertEqual(countSumTo(self.A, 7), 2)

    def test_B8(self):
        self.assertEqual(countSumTo(self.B, 8), 3)

if __name__ == '__main__':
    unittest.main()
