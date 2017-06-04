import unittest

b32 = 0xFFFFFFFF

def bitInsertionFor(N, M, i, j):
    clearmask = 0
    for b in range(i, j):
        clearmask |= 1 << b
    clearmask = ~clearmask
    r = N & clearmask
    return r | (M << i)

def bitInsertionBit(N, M, i, j):
    clearmask = (~1 & b32) << j
    clearmask |= (1 << i) - 1
    R = N & clearmask
    R |= (M << i)
    return R


class Playground(unittest.TestCase):
    def setUp(self):
        self.A = [
                dict(N=0b10000000000, M=0b10011, i=2, j=6, E=0b10001001100),
                dict(N=0b10000000000, M=0b10011, i=1, j=5, E=0b10000100110),
                dict(N=0b11111111111, M=0b10011, i=1, j=5, E=0b11111100111),
                dict(N=0b11111111111, M=0b10011, i=1, j=5, E=0b11111100111),
                ]

    def runAllTests(self, method):
        for test in self.A:
            N = test['N'] 
            M = test['M'] 
            i = test['i'] 
            j = test['j'] 
            E = test['E'] 
            self.assertEqual(bin(method(N, M, i, j)), bin(E))

    def test_example_for(self):
        self.runAllTests(bitInsertionFor)

    def test_example_bit(self):
        self.runAllTests(bitInsertionBit)

if __name__ == '__main__':
    unittest.main()
