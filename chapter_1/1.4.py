import unittest

def is_palindrome_permutation(text):
    def calcFrequencies(text):
        freq = {}
        for ch in text:
            if not ch in [' ']:
                freq[ch] = freq.get(ch, 0) + 1
        return freq

    freq = calcFrequencies(text)
    hasOdd = False
    for f in freq.values():
        if (f % 2) == 1:
            if hasOdd:
                # Only one odd case may occour: the middle element
                return False
            hasOdd = True
    return True

class Playground(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_palindrome_permutation('taco cat'))

    def test_2(self):
        self.assertFalse(is_palindrome_permutation('cat'))

    def test_3(self):
        self.assertTrue(is_palindrome_permutation('ama'))

    def test_4(self):
        self.assertTrue(is_palindrome_permutation('mirrim'))

    def test_5(self):
        self.assertFalse(is_palindrome_permutation('mirtxrim'))

if __name__ == '__main__':
    unittest.main()
