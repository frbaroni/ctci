import unittest

def compress(text):
    char = text[1]
    count = 0
    result = ''
    for i in range(len(text)):
        if text[i] != char:
            result += '{0}{1}'.format(char, count)
            count = 0
            char = text[i]
        count += 1
    if count > 0:
        result += '{0}{1}'.format(char, count)
    return result if len(result) < len(text) else text


class Playground(unittest.TestCase):
    def test_1(self):
        self.assertEqual(compress('aabcccccaaa'), 'a2b1c5a3')
    def test_2(self):
        self.assertEqual(compress('abcd'), 'abcd')


if __name__ == '__main__':
    unittest.main()
