import unittest
import re


class TestPart(unittest.TestCase):
    def test_example(self):
        test_in = """0 1 10 99 999"""

        out = 7

        self.assertEqual(process(test_in, 1), out)

    def test_example2(self):
        test_in = """125 17"""

        out = 55312

        self.assertEqual(process(test_in, 6), 22)
        self.assertEqual(process(test_in, 25), out)


def apply_rules(stone):
    if stone == 0:
        return [1]

    stone_string = str(stone)
    stone_len = len(stone_string)
    if not stone_len % 2:
        return [
            int(stone_string[: stone_len // 2]),
            int(stone_string[stone_len // 2 :]),
        ]

    return [stone * 2024]


def process(input, blinks):
    total = 0

    original_stones = list(map(int, input.split()))

    cur_stones = original_stones[:]
    for times in range(blinks):
        new_stones = []
        for stone in cur_stones:
            new_stones.extend(apply_rules(stone))
        cur_stones = new_stones[:]

    total = len(cur_stones)

    return total


if __name__ == "__main__":
    if unittest.main(exit=False).result.wasSuccessful():
        file_content = None
        with open("input.txt") as infile:
            file_content = infile.read()

        file_content = file_content[:-1]  # Strip trailing newline
        output = process(file_content, 25)
        print(f"Ans: {output}")
