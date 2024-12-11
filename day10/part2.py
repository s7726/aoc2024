import unittest
import re
from itertools import product


class TestPart(unittest.TestCase):
    def test_example(self):
        test_in = """.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9...."""

        out = 3

        self.assertEqual(process(test_in), out)

    def test_example2(self):
        test_in = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""

        out = 13

        self.assertEqual(process(test_in), out)

    def test_example3(self):
        test_in = """012345
123456
234567
345678
4.6789
56789."""

        out = 227

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

        out = 81

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
    score = 0

    current_location = trail_map[start[0]][start[1]]

    try:
        if int(current_location) != index:
            return 0
    except ValueError:
        return 0

    if current_location == "9":
        return 1

    locations = [(start[0] + y, start[1] + x) for y, x in DIRS]
    try:
        locations.remove(entry)
    except ValueError:
        pass
    next_locations = [loc for loc in locations if point_in_bounds(trail_map, loc)]

    for next_start in next_locations:
        found = find_trail(trail_map, start, next_start, index=index + 1)
        score += found

    return score


def process(input):
    total = 0
    trail_map = []

    for line in input.split("\n"):
        trail_map.append([c for c in line])

    print_board(trail_map)

    accessible_nines = 0

    for row in range(len(trail_map)):
        for col in range(len(trail_map[row])):
            if trail_map[row][col] == "0":
                accessible_nines += find_trail(trail_map, (-1, -1), (row, col))

    total = accessible_nines

    return total


if __name__ == "__main__":
    if unittest.main(exit=False).result.wasSuccessful():
        file_content = None
        with open("input.txt") as infile:
            file_content = infile.read()

        file_content = file_content[:-1]  # Strip trailing newline
        output = process(file_content)
        print(f"Ans: {output}")
