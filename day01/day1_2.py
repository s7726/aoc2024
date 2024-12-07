import unittest
import re

class TestPart2(unittest.TestCase):
    def test_example(self):
        test_in = """3   4
4   3
2   5
1   3
3   9
3   3"""

        out = 31

        self.assertEqual(process(test_in), out)

def process(input):
    total = 0

    first = []
    second = []
    in_list = re.findall(r'(\d+)\s+(\d+)', input)
    
    for item in in_list:
        first.append(int(item[0]))
        second.append(int(item[1]))

    appearances = {}

    first.sort()
    second.sort()
    for x in first:
        appearances[x] = 0
        for y in second:
            if x == y:
                appearances[x] += 1


    for num in first:
        total += num * appearances[num]

    return total


if __name__ == '__main__':
    if unittest.main(exit=False).result.wasSuccessful():
        file_content = None
        with open('input.txt') as infile:
            file_content = infile.read()
        output = process(file_content)
        print(f'Ans: {output}')