import unittest
import re


class TestPart(unittest.TestCase):
    def test_example(self):
        test_in = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

        out = 41

        self.assertEqual(process(test_in), out)


def print_board(board):
    for row in range(len(board)):
        for col in range(len(board)):
            print(board[row][col], end="")
        print()


# N E S W
DIRS = [(-1, 0), (0, +1), (+1, 0), (0, -1)]


def add_dir(r, c, dir_indx):
    return tuple(map(sum, zip((r, c), DIRS[dir_indx])))


def move(board, r, c, dir_indx):
    alive = True
    board[r][c] = "X"

    new_r, new_c = (r, c)
    new_dir_indx = dir_indx

    for i in range(len(DIRS)):
        new_r, new_c = add_dir(r, c, new_dir_indx)

        try:
            if (
                new_r < 0
                or new_r > len(board) - 1
                or new_c < 0
                or new_c > len(board[new_r])
            ):
                alive = False
            elif board[new_r][new_c] == "#":
                new_dir_indx = (new_dir_indx + 1) % len(DIRS)
                new_r, new_c = add_dir(r, c, new_dir_indx)
            else:
                break
        except IndexError:
            alive = False

    return new_r, new_c, new_dir_indx, alive


def find_start(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "^":
                return row, col
    return None, None


def count_x(board):
    x = 0
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "X":
                x += 1
    return x


def process(input):
    total = 0

    board = [list(l) for l in input.splitlines()]

    row, col = find_start(board)

    alive = True
    dir_indx = 0
    while alive:
        row, col, dir_indx, alive = move(board, row, col, dir_indx)

    print_board(board)

    total = count_x(board)

    return total


if __name__ == "__main__":
    if unittest.main(exit=False).result.wasSuccessful():
        file_content = None
        with open("input.txt") as infile:
            file_content = infile.read()
        output = process(file_content)
        print(f"Ans: {output}")
