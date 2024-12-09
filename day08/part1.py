import unittest
import re
from itertools import combinations
from math import sqrt
import math
from copy import deepcopy
from pprint import pprint


class TestPart(unittest.TestCase):
    def test_example(self):
        test_in = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

        out = 14

        self.assertEqual(process(test_in), out)

    def test_example2(self):
        test_in = """..........
...#......
..........
....a.....
..........
.....a....
..........
......#...
..........
.........."""

        out = 2

        self.assertEqual(process(test_in), out)

    def test_example3(self):
        test_in = """..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......#...
..........
.........."""

        out = 4

        self.assertEqual(process(test_in), out)

    def test_example4(self):
        test_in = """..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......A...
..........
..........
"""

        out = 4

        self.assertEqual(process(test_in), out)

    def test_new_point(self):
        self.assertEqual(new_points_at_slope_dist((0, 0), 1, 2), [(2, 2), (-2, -2)])


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


def euclid_dist(a, b):
    return sqrt((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]))


def slope(a, b):
    return (a[0] - b[0]) / (a[1] - b[1])


def point_in_bounds(board, point):
    return (not (point[0] < 0 or point[0] > (len(board) - 1))) and (
        not (point[1] < 0 or point[1] > (len(board[0]) - 1))
    )


def point_not_between_antennas(antenna_pairing, point):
    sorted_pairing = sorted(list(antenna_pairing))
    left = point[1] >= antenna_pairing[0][1]
    right = point[1] <= antenna_pairing[1][1]
    top = point[0] >= antenna_pairing[0][0]
    bottom = point[0] <= antenna_pairing[0][1]

    return not (top or right or left or bottom)


def tuple_add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def tuple_subtract(a, b):
    return tuple(x - y for x, y in zip(a, b))


def new_gridpoints_from_start(point, grid_distance):
    return [tuple_add(point, grid_distance), tuple_subtract(point, grid_distance)]


def new_points_at_slope_dist(point, sl, dist):
    """lifted largely from https://www.geeksforgeeks.org/find-points-at-a-given-distance-on-a-line-of-given-slope/"""
    # slope is 0
    a = [0, 0]
    b = [0, 0]
    if sl == 0:
        a[1] = point[1] + dist
        a[0] = point[0]

        b[1] = point[1] - dist
        b[0] = point[0]

    # if slope is infinite
    elif math.isfinite(sl) is False:
        a[1] = point[1]
        a[0] = point[0] + dist

        b[1] = point[1]
        b[0] = point[0] - dist
    else:
        dx = dist / math.sqrt(1 + (sl * sl))
        dy = sl * dx
        a[1] = math.ceil(point[1] + dx)
        a[0] = math.ceil(point[0] + dy)
        b[1] = math.floor(point[1] - dx)
        b[0] = math.floor(point[0] - dy)

    return [tuple(a), tuple(b)]


def process(input):
    total = 0
    node_mat = []

    for line in input.split("\n"):
        node_mat.append([c for c in line])

    anode_map = deepcopy(node_mat)

    valid_antenna = re.compile(r"[a-zA-Z\d]")

    freqs = {}
    freq_pairs = {}
    for row in range(len(node_mat)):
        for col in range(len(node_mat[row])):
            pos_val = node_mat[row][col]
            if valid_antenna.match(pos_val):
                if not pos_val in freqs:
                    freqs[pos_val] = []
                freqs[pos_val].append((row, col))

    anode_points = []

    for freq, antennas in freqs.items():
        antenna_pairings = list(combinations(antennas, 2))
        freq_pairs[freq] = antenna_pairings

        for antenna_pairing in antenna_pairings:
            dist = gridpoint_distance(*antenna_pairing)

            for point in antenna_pairing:
                new_points = new_gridpoints_from_start(point, dist)
                new_points = [
                    p
                    for p in new_points
                    if p not in antenna_pairing
                    and point_in_bounds(node_mat, p)
                    and not point_not_between_antennas(antenna_pairing, p)
                ]
                anode_points.extend(new_points)
    pprint(freq_pairs)
    unique_anodes = sorted(list(set(anode_points)))
    print(f"{unique_anodes=}::{len(unique_anodes)}")

    fill_board(anode_map, unique_anodes)
    print_board(anode_map)

    total = len(unique_anodes)

    return total


if __name__ == "__main__":
    if unittest.main(exit=False).result.wasSuccessful():
        file_content = None
        with open("input.txt") as infile:
            file_content = infile.read()

        file_content = file_content[:-1]
        output = process(file_content)
        print(f"Ans: {output}")
