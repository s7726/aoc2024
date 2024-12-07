import unittest
import re

class TestPart(unittest.TestCase):
    def test_example(self):
        test_in = """
"""

        out = 2

        self.assertEqual(process(test_in), out)

def process(input):
    total = 0

    
    return total


if __name__ == '__main__':
    if unittest.main(exit=False).result.wasSuccessful():
        file_content = None
        with open('input.txt') as infile:
            file_content = infile.read()
        output = process(file_content)
        print(f'Ans: {output}')