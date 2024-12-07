import unittest
import re

class TestPart(unittest.TestCase):
    def test_example(self):
        test_in = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

        out = 2

        self.assertEqual(process(test_in), out)

def process(input):
    total = 0

    lines = input.split('\n')

    for l in lines:
        if not len(l):
            continue
        line = list(map(int, l.split(' ')))

        print(line)
        if line == sorted(line) or line == sorted(line, reverse=True):
            goodline = True
            pairs = zip(line, line[1:])
            def good(a_):
                a = int(a_[0])
                b = int(a_[1])
                diff = abs(a - b)

                return diff >= 1 and diff <= 3
            for pair in pairs:
                if not good(pair):
                    goodline = False
            total += goodline
    
    return total


if __name__ == '__main__':
    if unittest.main(exit=False).result.wasSuccessful():
        file_content = None
        with open('input.txt') as infile:
            file_content = infile.read()
        output = process(file_content)
        print(f'Ans: {output}')