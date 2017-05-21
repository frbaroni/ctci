import unittest
from mylist import LinkedList

def palindromeList(head):
    def check(node, state):
        if not state['finished']:
            snode = state['node']
            state['node'] = snode.next
            if node.data == snode.data:
                if node == snode:
                    state['finished'] = True
            else:
                state['palindrome'] = False
    def sapply(node, state):
        if node is not None:
            sapply(node.next, state)
            check(node, state)
    state = {'node': head, 'finished': False, 'palindrome': True}
    sapply(head, state)
    return state['palindrome'] 
    

class Playground(unittest.TestCase):
    def test_valid(self):
        A = LinkedList.create([1, 1, 2, 1, 1])
        E = True
        self.assertEqual(palindromeList(A), E)

    def test_valid_2(self):
        A = LinkedList.create([1, 2, 3, 3, 2, 1])
        E = True
        self.assertEqual(palindromeList(A), E)

    def test_invalid(self):
        A = LinkedList.create([1, 2, 3, 1])
        E = False
        self.assertEqual(palindromeList(A), E)

if __name__ == '__main__':
    unittest.main()
