import unittest
import re


class TestPart(unittest.TestCase):
    def test_example(self):
        test_in = """"""

        out = 2

        self.assertEqual(process(test_in), out)


def process(input):
    total = 0

    return total


def input_runner(input):
    """This exists to provide a cleaner place to feed puzzle specific arguments
    to the process function
    """

    return process(input)


if __name__ == "__main__":
    if unittest.main(exit=False).result.wasSuccessful():
        file_content = None
        with open("input.txt") as infile:
            file_content = infile.read()

        file_content = file_content[:-1]  # Strip trailing newline
        import time

        start_time = time.time()
        output = input_runner(file_content)

        print(f"=======  {(time.time() - start_time):.3f}s  ======")
        print(f"Ans: {output}")
