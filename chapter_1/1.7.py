import unittest

def rotate(M):
    def rotate_inplace(left, top, right, bottom):
        for i in range(int((right - left) / 2) + 1):
            tmp = M[top][left + i]
            M[top][left + i] = M[bottom][left + i]
            M[bottom][left + i] = M[bottom][right - i]
            M[bottom][right - i] = M[top][right - i]
            M[top][right - i] = tmp
    def rotate_matrix(left, top, right, bottom):
        if not ((right < left) or (bottom < top)):
            rotate_inplace(left, top, right, bottom)
            rotate_matrix(left + 1, top + 1, right - 1, bottom - 1)
    rotate_matrix(0, 0, len(M[0]) -1, len(M) - 1)
    return M


class Playground(unittest.TestCase):
    def test_1(self):
        matrix = [
                [1,2,3],
                [4,5,6],
                [7,8,9]]
        expected = [
                [7,4,1],
                [8,5,2],
                [9,6,3]]
        self.assertEqual(rotate(matrix), expected)

if __name__ == '__main__':
    unittest.main()
