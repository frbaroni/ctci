import unittest

def one_way(a, b):
    def single_edit(a, b):
        diff = False
        i = j = 0
        while i < len(a):
            if a[i] != b[j]:
                if diff:
                    return False
                else:
                    diff = True
                if len(a) != len(b):
                    i += 1
            j += 1
            i += 1
        return True

    if len(a) > len(b):
        return one_way(b, a)
    else:
        if abs(len(a) - len(b)) > 1:
            return False
        else:
            return single_edit(a, b)



class Playground(unittest.TestCase):
    def test_1(self):
        self.assertTrue(one_way('pale', 'ple'))

    def test_2(self):
        self.assertTrue(one_way('pales', 'pale'))

    def test_3(self):
        self.assertTrue(one_way('pale', 'bale'))

    def test_4(self):
        self.assertFalse(one_way('pale', 'bake'))

if __name__ == '__main__':
    unittest.main()
