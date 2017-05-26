import unittest
from mytree import Tree

def depthLists(tree):
    def depthListsAcc(node, levels, level):
        if node is not None:
            depthListsAcc(node.left, levels, level + 1)
            if not level in levels:
                levels[level] = []
            levels[level].append(node)
            depthListsAcc(node.right, levels, level + 1)
        return levels
    return depthListsAcc(tree, {}, 0)

class Playground(unittest.TestCase):
    @staticmethod
    def nodeValues(nodes):
        return [node.value for node in nodes]

    def test_depth_perfect(self):
        level1 = [      50      ]
        level2 = [  25,     75  ]
        level3 = [10, 40, 65, 80]
        E = Tree.create_like([
            level1,
            level2,
            level3
            ])
        levels = depthLists(E)
        self.assertEqual(self.nodeValues(levels[0]), level1)
        self.assertEqual(self.nodeValues(levels[1]), level2)
        self.assertEqual(self.nodeValues(levels[2]), level3)

    def test_depth_not_perfect(self):
        level1 = [      50      ]
        level2 = [  25,     75  ]
        level3 = [10, 40, 65, None]
        E = Tree.create_like([
            level1,
            level2,
            level3
            ])
        level3 = level3[:3]
        levels = depthLists(E)
        self.assertEqual(self.nodeValues(levels[0]), level1)
        self.assertEqual(self.nodeValues(levels[1]), level2)
        self.assertEqual(self.nodeValues(levels[2]), level3)

if __name__ == '__main__':
    unittest.main()
