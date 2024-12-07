import unittest
import collections

collections.Callable = collections.abc.Callable  # type: ignore


class TestPart(unittest.TestCase):
    def test_example(self):
        test_in = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

        out = 9

        self.assertEqual(process(test_in), out)


xmas = [c for c in "XMAS"]

DIRS = {
    "NW": (-1, -1),
    "N": (0, -1),
    "NE": (+1, -1),
    "W": (-1, 0),
    "E": (+1, 0),
    "SW": (-1, +1),
    "S": (0, +1),
    "SE": (+1, +1),
}


def fx(mat, in_x, in_y, of_x, of_y, i=0):
    x = in_x + of_x
    y = in_y + of_y
    try:
        if x < 0 or y < 0 or y > len(mat) or x > len(mat[y]):
            return ""

        return mat[y][x]
    except IndexError:
        return ""


def process(input):
    total = 0
    mat = []

    for line in input.split("\n"):
        mat.append([c for c in line])

    for row in range(len(mat)):
        for col in range(len(mat[row])):
            if mat[row][col] == "A":
                nw = fx(mat, col, row, *DIRS["NW"])
                ne = fx(mat, col, row, *DIRS["NE"])
                sw = fx(mat, col, row, *DIRS["SW"])
                se = fx(mat, col, row, *DIRS["SE"])
                if (nw == "M" and se == "S" or nw == "S" and se == "M") and (
                    ne == "M" and sw == "S" or ne == "S" and sw == "M"
                ):
                    # print(f"@{f'{col:>3},{row:<3}':<8}\t{direction}\t{offsets}")
                    total += 1

    return total


if __name__ == "__main__":
    if unittest.main(exit=False).result.wasSuccessful():
        file_content = None
        with open("input.txt") as infile:
            file_content = infile.read()
        output = process(file_content)
        print(f"Ans: {output}")
