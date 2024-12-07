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

        out = 4

        self.assertEqual(process(test_in), out)

def goodline(line):
    good = False
    if line == sorted(line) or line == sorted(line, reverse=True):
        good = True
        pairs = zip(line, line[1:])
        def good_diff(a_):
            a = a_[0]
            b = a_[1]
            diff = abs(a - b)

            return diff >= 1 and diff <= 3
        for pair in pairs:
            if not good_diff(pair):
                good = False
    return good

def process(input):
    total = 0

    lines = input.split('\n')

    for l in lines:
        goodness = 0
        if not len(l):
            continue
        origline = list(map(int, l.split(' ')))

        for x in range(len(origline)):
            line = origline[:x] + origline[x+1:]
            goodness += goodline(line)
        total += (goodness > 0)

    return total


if __name__ == '__main__':
    if unittest.main(exit=False).result.wasSuccessful():
        file_content = None
        with open('input.txt') as infile:
            file_content = infile.read()
        output = process(file_content)
        print(f'Ans: {output}')