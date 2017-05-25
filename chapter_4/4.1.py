import unittest
import collections
from mygraph import GraphNode

def hasRoute(origin, destination):
    visited = set()
    queue = collections.deque()
    queue.append(origin)
    while len(queue) > 0:
        node = queue.popleft()
        if node == destination:
            return True
        visited.add(node)
        for child in node.children:
            if not child in visited:
                queue.append(child)
    return False

class Playground(unittest.TestCase):
    def test_has_route(self):
        nodes = GraphNode.create([
            'a -> b',
            'b -> c',
            'c -> d',
            'd -> e',
            'e -> f',
            'a -> c',
            'h -> j'
            ])
        self.assertTrue(hasRoute(nodes['a'], nodes['e']))
        self.assertTrue(hasRoute(nodes['c'], nodes['f']))
        self.assertTrue(hasRoute(nodes['f'], nodes['b']))
        self.assertTrue(hasRoute(nodes['j'], nodes['h']))
        self.assertFalse(hasRoute(nodes['h'], nodes['a']))

if __name__ == '__main__':
    unittest.main()
