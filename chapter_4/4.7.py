import unittest
import copy
from mytree import Tree

def buildOrder(projects, deps):
    reqs = {proj: [] for proj in projects}
    dependents = copy.deepcopy(reqs)
    for (dependency, dependent) in deps:
        reqs[dependent].append(dependency)
        dependents[dependency].append(dependent)
    order = []
    while len(reqs) > 0:
        found = False
        for p in projects:
            if not p in reqs:
                continue
            if len(reqs[p]) == 0:
                order.append(p)
                for d in dependents[p]:
                    reqs[d].remove(p)
                found = True
                reqs.pop(p)
                break
        if not found:
            return None
    return order
            

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


if __name__ == '__main__':
    unittest.main()
