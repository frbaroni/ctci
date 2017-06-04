import unittest
from collections import defaultdict
from mytree import Tree

def countSumToBruteforce(head, sumTo):
    def sub(node, current_sum, total_sum):
        if node:
            value = current_sum + node.value
            if value == sumTo:
                total_sum += 1
            total_sum = sub(node.left, value, total_sum)
            total_sum = sub(node.right, value, total_sum)
            if head != node:
                total_sub_sum = countSumToBruteforce(node, sumTo)
                total_sum += total_sub_sum
        return total_sum

    return sub(head, 0, 0)

def countSumToMemoized(head, sumTo):
    def sub(node, current_sum, path_sums):
        if not node:
            return 0

        current_sum += node.value
        wanted_sum = current_sum - sumTo
        total_sum = path_sums.get(wanted_sum, 0)

        if current_sum == sumTo:
            total_sum += 1

        path_sums[current_sum] += 1

        total_sum += sub(node.left, current_sum, path_sums)
        total_sum += sub(node.right, current_sum, path_sums)

        path_sums[current_sum] -= 1

        return total_sum

    return sub(head, 0, defaultdict(lambda: 0))

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

    def test_A5_Bruteforce(self):
        self.assertEqual(countSumToBruteforce(self.A, 5), 2)

    def test_A7_Bruteforce(self):
        self.assertEqual(countSumToBruteforce(self.A, 7), 2)

    def test_B8_Bruteforce(self):
        self.assertEqual(countSumToBruteforce(self.B, 8), 3)

    def test_A5_Memoized(self):
        self.assertEqual(countSumToMemoized(self.A, 5), 2)

    def test_A7_Memoized(self):
        self.assertEqual(countSumToMemoized(self.A, 7), 2)

    def test_B8_Memoized(self):
        self.assertEqual(countSumToMemoized(self.B, 8), 3)


if __name__ == '__main__':
    unittest.main()
