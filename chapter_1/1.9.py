import unittest

def isStringRotation(a, b):
    return (b + b).find(a) != -1

class Playground(unittest.TestCase):
    def test_0(self):
        self.assertTrue(isStringRotation('waterloo', 'terloowa'))

    def test_1(self):
        self.assertTrue(isStringRotation('test', 'estt'))

    def test_2(self):
        self.assertFalse(isStringRotation('test', 'tset'))

if __name__ == '__main__':
    unittest.main()
