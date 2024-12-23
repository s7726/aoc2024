import unittest
import re
from functools import cache


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


def list_halfs(input):
    left, right = input[: len(input) // 2], input[len(input) // 2 :]
    if len(left) == 0 or len(right) == 0:
        pass
    return input[: len(input) // 2], input[len(input) // 2 :]


@cache
def process_depth(input_s, blinks, depth):
    input = list(map(int, input_s.split()))
    total = 0
    cur_depth = 0
    added_len = 0
    if blinks == 0 or depth == 0 or len(input) == 0:
        return 0

    print(f"D={len(input)}:{blinks}:{depth}", flush=True)

    this_hunk = []

    if len(input) < 2:
        this_hunk, cur_depth = process_hunk(input, min(20, blinks))

    blinks_remaining = blinks - cur_depth
    depth_remaining = depth - cur_depth

    if blinks_remaining == 0 or depth_remaining == 0:
        total += len(this_hunk)
        return total

    if len(this_hunk) == 0:
        this_hunk = input

    left, right = list_halfs(this_hunk)

    for i in left:
        total += process_depth(str(i), blinks_remaining, depth_remaining)
    for j in right:
        total += process_depth(str(j), blinks_remaining, depth_remaining)

    return total


def process_hunk(input, blinks):
    total = 0
    times = 0
    cur_stones = input[:]
    for times in range(blinks):
        new_stones = []
        print(f"H={len(cur_stones)}:{blinks - times}")
        for stone in cur_stones:
            new_stones.extend(apply_rules(stone))
        cur_stones = new_stones

    return cur_stones, times + 1


def process(input, blinks):
    return process_depth(input, blinks, blinks)


def input_runner(input):
    """This exists to provide a cleaner place to feed puzzle specific arguments
    to the process function
    """

    return process(input, 75)


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
