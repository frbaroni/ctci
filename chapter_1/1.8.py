import unittest

class zerinM:
    def __init__(self, M):
        self.M = M
        self.rows = len(M)
        self.cols = len(M[0])

    def nullcol(self, y):
        for x in range(0, self.cols):
            self.M[y][x] = 0

    def nullrow(self, x):
        for y in range(0, self.rows):
            self.M[y][x] = 0

    def findZeros(self):
        for x in range(1, self.cols):
            for y in range(1, self.rows):
                if self.M[y][x] == 0:
                    self.M[y][0] = 0
                    self.M[0][x] = 0
    
    def zeroRows(self):
        for y in range(1, self.rows):
            if self.M[y][0] == 0:
                self.nullrow(y)

    def zeroCols(self):
        for x in range(1, self.rows):
            if self.M[0][x] == 0:
                self.nullcol(x)

    def check0RowCol(self):
        self.row0has0 = any((self.M[y][0] == 0) for y in range(self.rows))
        self.col0has0 = any((self.M[0][x] == 0) for x in range(self.cols))

    def zero0RowCol(self):
        if self.row0has0: self.nullrow(0)
        if self.col0has0: self.nullcol(0)

    def __call__(self):
        self.check0RowCol()
        self.findZeros()
        self.zeroRows()
        self.zeroCols()
        self.zero0RowCol()
        return self.M

def zerin(M):
    return zerinM(M)()

class Playground(unittest.TestCase):
    def test_0_0(self):
        m = zerinM([
            [1,2,3],
            [4,5,6],
            [7,8,9]
            ])
        m.check0RowCol()
        self.assertFalse(m.row0has0)
        self.assertFalse(m.col0has0)

    def test_0_1(self):
        m = zerinM([
            [1,0,3],
            [4,5,6],
            [7,8,9]
            ])
        m.check0RowCol()
        self.assertFalse(m.row0has0)
        self.assertTrue(m.col0has0)

    def test_0_2(self):
        m = zerinM([
            [1,2,3],
            [4,5,6],
            [0,8,9]
            ])
        m.check0RowCol()
        self.assertTrue(m.row0has0)
        self.assertFalse(m.col0has0)

    def test_0_3(self):
        m = zerinM([
            [1,2,3],
            [4,0,6],
            [7,8,9]
            ])
        m.check0RowCol()
        m.findZeros()
        self.assertFalse(m.row0has0)
        self.assertFalse(m.col0has0)
        self.assertEqual(m.M, [
            [1,0,3],
            [0,0,6],
            [7,8,9]
            ])

    def test_0_4(self):
        m = zerinM([
            [1,2,3],
            [4,0,6],
            [7,8,9]
            ])
        m.check0RowCol()
        m.findZeros()
        self.assertFalse(m.row0has0)
        self.assertFalse(m.col0has0)
        self.assertEqual(m.M, [
            [1,0,3],
            [0,0,6],
            [7,8,9]
            ])

    def test_1_1(self):
        matrix = [
                [1,2,3],
                [4,5,0],
                [7,8,9]
                ]
        expected = [
                [1,2,0],
                [0,0,0],
                [7,8,0]
                ]
        self.assertEqual(zerin(matrix), expected)

    def test_1_2(self):
        matrix = [
                [1,0,3],
                [4,5,6],
                [7,8,9]
                ]
        expected = [
                [0,0,0],
                [4,0,6],
                [7,0,9]
                ]
        self.assertEqual(zerin(matrix), expected)

    def test_1_3(self):
        matrix = [
                [1,2,3],
                [0,5,6],
                [7,8,9]
                ]
        expected = [
                [0,2,3],
                [0,0,0],
                [0,8,9]
                ]
        self.assertEqual(zerin(matrix), expected)

    def test_1_4(self):
        matrix = [
                [0,2,3],
                [4,5,6],
                [7,8,9]
                ]
        expected = [
                [0,0,0],
                [0,5,6],
                [0,8,9]
                ]
        self.assertEqual(zerin(matrix), expected)

if __name__ == '__main__':
    unittest.main()
