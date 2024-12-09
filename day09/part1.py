import unittest
import re


class TestPart(unittest.TestCase):
    def test_example(self):
        test_in = """2333133121414131402"""

        out = 1928

        self.assertEqual(process(test_in), out)


def move_files_to_empty_space(disk):
    rdisk = [i for i in disk[::-1] if i != "."]
    ndisk = ["."] * len(rdisk)
    for i, item in enumerate(disk):
        if item == ".":
            try:
                ndisk[ndisk.index(".")] = rdisk.pop(0)
            except IndexError:
                break
        else:
            try:
                ndisk[i] = item
            except IndexError:
                break

    ndisk.extend(["."] * (len(disk) - len(ndisk)))

    return ndisk


def checksum(disk):
    return sum([int(x) * i for i, x in enumerate(disk) if x != "."])


def process(input):
    total = 0

    files = input[::2]
    fileid = list(range(len(files)))
    freespace = input[1::2]

    udisk = []
    for i, size in enumerate(input):
        if i % 2:
            udisk.extend(["."] * int(size))
        else:
            udisk.extend([f"{fileid.pop(0)}"] * int(size))

    sdisk = move_files_to_empty_space(udisk)

    # print(f"{files=}\n{fileid}\n{freespace=}\n{udisk=}")
    print(f"{''.join(udisk)}")
    print(f"{''.join(sdisk)}")

    total = checksum(sdisk)

    return total


if __name__ == "__main__":
    if unittest.main(exit=False).result.wasSuccessful():
        file_content = None
        with open("input.txt") as infile:
            file_content = infile.read()

        file_content = file_content[:-1]
        output = process(file_content)
        print(f"Ans: {output}")
