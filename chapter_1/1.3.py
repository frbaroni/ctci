import unittest

def urlify(text):
    for i in reversed(range(0, len(text))):
        if text[i] != ' ':
            text = list(text)
            j = len(text) - 1
            while j >= 0:
                if text[i] == ' ':
                    text[j] = '0'
                    text[j-1] = '2'
                    text[j-2] = '%'
                    j -= 2
                else:
                    text[j] = text[i]
                j -= 1
                i -= 1
            return ''.join(text)
    return text

class Playground(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(urlify('Mr John Smith    '), 'Mr%20John%20Smith')

if __name__ == '__main__':
    unittest.main()
