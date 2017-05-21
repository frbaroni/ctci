import unittest
from mylist import LinkedList

def loopPoint(head):
    slow = head
    fast = head
    while True:
        end = (fast is None) or (fast.next is None)
        if end:
            return None
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast

class Playground(unittest.TestCase):
    def test_no_loop(self):
        A = LinkedList.create([1, 2, 3, 4, 5])
        E = None
        self.assertEqual(loopPoint(A), E)

    def test_loop(self):
        A = LinkedList.create([1, 2, 3, 4, 5])
        A.next.next.next.next.next = A.next.next.next
        E = A.next.next.next
        self.assertEqual(loopPoint(A), E)

if __name__ == '__main__':
    unittest.main()
