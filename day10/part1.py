import unittest
import re
from itertools import product


class TestPart(unittest.TestCase):
    def test_example(self):
        test_in = """0123
1234
8765
9876"""

        out = 1

        # self.assertEqual(process(test_in), out)

    def test_example2(self):
        test_in = """...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9"""

        out = 2

        self.assertEqual(process(test_in), out)

    def test_example3(self):
        test_in = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""

        out = 4

        self.assertEqual(process(test_in), out)

    def test_example4(self):
        test_in = """10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01"""

        out = 3

        self.assertEqual(process(test_in), out)

    def test_example5(self):
        test_in = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

        out = 36

        self.assertEqual(process(test_in), out)


def print_board(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(board[row][col], end="")
        print()


def fill_board(board, points, char="#"):
    for point in points:
        try:
            board[point[0]][point[1]] = char
        except IndexError:
            print(f"ERROR: {point}")
            raise IndexError


def gridpoint_distance(a, b):
    return (b[0] - a[0], b[1] - a[1])


DIRS = [
    (0, -1),
    (-1, 0),
    (+1, 0),
    (0, +1),
]


def point_in_bounds(board, point):
    return (point[0] >= 0 and point[0] <= (len(board) - 1)) and (
        point[1] >= 0 and point[1] <= (len(board[0]) - 1)
    )


def tuple_subtract(a, b):
    return tuple(x - y for x, y in zip(a, b))


def find_trail(trail_map, entry, start, index=0):
    score = []

    current_location = trail_map[start[0]][start[1]]

    try:
        if int(current_location) != index:
            return None
    except ValueError:
        return None

    if current_location == "9":
        return start

    locations = [(start[0] + y, start[1] + x) for y, x in DIRS]
    try:
        locations.remove(entry)
    except ValueError:
        pass
    next_locations = [loc for loc in locations if point_in_bounds(trail_map, loc)]

    for next_start in next_locations:
        found = find_trail(trail_map, start, next_start, index=index + 1)
        if isinstance(found, tuple):
            score.append(found)
        elif isinstance(found, list):
            score.extend(found)

    return score


def process(input):
    total = 0
    trail_map = []

    for line in input.split("\n"):
        trail_map.append([c for c in line])

    print_board(trail_map)

    accessible_nines = {}

    for row in range(len(trail_map)):
        for col in range(len(trail_map[row])):
            if trail_map[row][col] == "0":
                accessible_nines[(row, col)] = []
                accessible_nines[(row, col)].extend(
                    find_trail(trail_map, (-1, -1), (row, col))
                )

    unique_nines = {k: list(set(v)) for k, v in accessible_nines.items()}
    scores = {k: len(v) for k, v in unique_nines.items()}

    total = sum([v for v in scores.values()])

    return total


if __name__ == "__main__":
    if unittest.main(exit=False).result.wasSuccessful():
        file_content = None
        with open("input.txt") as infile:
            file_content = infile.read()

        file_content = file_content[:-1]  # Strip trailing newline
        output = process(file_content)
        print(f"Ans: {output}")
