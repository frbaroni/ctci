import unittest
import random
import collections
from mytree import Tree

tree_items = [50, 25, 75, 10, 40, 65, 80]
tree = Tree.create_normal(tree_items)

# Cache 'size' on Tree insertion/remove
def tree_size(head):
    def count(node):
        if node is None:
            return 0
        else:
            return 1 + count(node.left) + count(node.right)
    return count(head)

def randomNode(head):
    def in_order(node, state):
        if node and (state['steps'] >= 0):
            if state['steps'] == 0:
                state['result'] = node
            state['steps'] -= 1
            in_order(node.left, state)
            in_order(node.right, state)
    total = tree_size(head)
    selected = random.randint(0, total - 1)
    state = dict(steps=selected, result=None)
    in_order(head, state)
    return state['result'] 


iterations = 10000
distribution = collections.defaultdict(lambda: 0)

for i in range(iterations):
    node = randomNode(tree)
    distribution[node.value] += 1

for value in tree_items:
    distributed = round((distribution[value] / iterations) * 100)
    print('{} -> {}'.format(value, distributed))
