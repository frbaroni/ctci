import unittest

def is_permutation(a, b):
    reorder = lambda text: ''.join(sorted(list(text)))
    return reorder(a) == reorder(b)

class Playground(unittest.TestCase):

    def test_permutation(self):
        self.assertTrue(is_permutation('debit card', 'bad credit'))

    def test_permutation_2(self):
        self.assertTrue(is_permutation('the eyes', 'they see'))

    def test_bad_permutation(self):
        self.assertFalse(is_permutation('anagram', 'amagram'))

    def test_bad_permutation_2(self):
        self.assertFalse(is_permutation('a b c d', 'a b d'))

if __name__ == '__main__':
    unittest.main()
