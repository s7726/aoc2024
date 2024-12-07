import unittest
import re

class TestPart1(unittest.TestCase):
    def test_example(self):
        test_in = """3   4
4   3
2   5
1   3
3   9
3   3"""

        out = 11

        self.assertEqual(process(test_in), out)

def process(input):
    first = []
    second = []
    in_list = re.findall(r'(\d+)\s+(\d+)', input)
    
    for item in in_list:
        first.append(int(item[0]))
        second.append(int(item[1]))

    first.sort()
    second.sort()
    total = 0
    for x, y in (zip(first, second)):
        total += abs(x-y)

    return total


if __name__ == '__main__':
    if unittest.main(exit=False).result.wasSuccessful():
        file_content = None
        with open('input.txt') as infile:
            file_content = infile.read()
        output = process(file_content)
        print(f'Ans: {output}')