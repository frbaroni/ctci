import unittest
import copy
import collections
from mytree import Tree

def buildOrder(projects, deps):
    reqs = {proj: [] for proj in projects}
    dependents = copy.deepcopy(reqs)
    for (dependency, dependent) in deps:
        reqs[dependent].append(dependency)
        dependents[dependency].append(dependent)
    independents = [p for p in projects if not reqs[p]]
    queue = collections.deque(independents)
    order = []
    while queue:
        p = queue.popleft()
        order.append(p)
        for d in projects:
            if d in dependents[p]:
                reqs[d].remove(p)
                if not reqs[d]:
                    queue.append(d)
    if len(projects) == len(order):
        return order
    else:
        return None
            

class Playground(unittest.TestCase):
    def test_build_order(self):
        projects = ['a', 'b', 'c', 'd', 'e', 'f']
        deps = [
                ('a', 'd'),
                ('f', 'b'),
                ('b', 'd'),
                ('f', 'a'),
                ('d', 'c'),
                ]
        output = ['e', 'f', 'a', 'b', 'd', 'c']

        self.assertEqual(buildOrder(projects, deps), output)

    def test_build_order_invalid(self):
        projects = ['a', 'b', 'c', 'd', 'e', 'f']
        deps = [
                ('a', 'd'),
                ('f', 'b'),
                ('b', 'd'),
                ('f', 'a'),
                ('d', 'c'),
                ('f', 'a'),
                ('e', 'b'),
                ]
        output = None

        self.assertEqual(buildOrder(projects, deps), output)


if __name__ == '__main__':
    unittest.main()
