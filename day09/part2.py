import unittest
import re


class TestPart(unittest.TestCase):
    def test_example(self):
        test_in = """2333133121414131402"""

        out = 2858

        self.assertEqual(process(test_in), out)

    def test_edge(self):
        """Thanks rust_dev0 for the edge case"""
        test_in = """2333133121414131401"""

        out = 2746

        self.assertEqual(process(test_in), out)


def flatten_disk(disk):
    return [x for xx in disk for x in xx]


def nested_disk_size(disk):
    return len(flatten_disk(disk))


def consolodate_empty_space(disk):
    for i, item in enumerate(disk):
        if len(item) == 0:
            disk.pop(i)
        elif item[0] == ".":
            try:
                if disk[i + 1][0] == ".":
                    new_item = disk[i] + disk[i + 1]
                    disk.pop(i + 1)
                    disk.pop(i)
                    disk.insert(i, new_item)
            except IndexError:
                break
    return disk


def move_files_to_empty_space(disk):
    disk_size = nested_disk_size(disk)

    rdisk = [i for i in disk[::-1] if len(i) and i[0] != "."]
    ndisk = disk[:]
    i = 0

    while True and i < len(rdisk):
        item = rdisk[i]
        try:
            empty_space = None
            j = 0
            for j in range(len(ndisk)):
                if (
                    ndisk[j] is not None
                    and ndisk[j][0] == "."
                    and len(ndisk[j]) >= len(item)
                ):
                    empty_space = j
                    break
            if empty_space is not None and empty_space < ndisk.index(item):
                empty_space_len = len(ndisk[empty_space])
                item_index = ndisk.index(item)
                ndisk.pop(ndisk.index(item))
                ndisk.insert(item_index, ["."] * (len(item)))

                ndisk[empty_space] = item
                ndisk.insert(empty_space + 1, ["."] * (empty_space_len - len(item)))

                rdisk_index = rdisk.index(item)
                rdisk.pop(rdisk.index(item))
                disk = consolodate_empty_space(ndisk)
                i = rdisk_index
            else:
                i += 1

        except IndexError:
            break
        except ValueError:
            continue

    ndisk.append(["."] * (disk_size - nested_disk_size(ndisk)))

    return ndisk


def checksum(disk):
    total = 0
    for i, x in enumerate(disk):
        if x != ".":
            total += int(x) * i
    total = total
    list_to_sum = [int(x) * i for i, x in enumerate(disk) if x != "."]
    return sum(list_to_sum)


def process(input):
    total = 0

    files = input[::2]
    fileid = list(range(len(files)))
    freespace = input[1::2]

    udisk = []
    for i, size in enumerate(input):
        if i % 2:
            udisk.append(["."] * int(size))
        else:
            udisk.append([f"{fileid.pop(0)}"] * int(size))

    sdisk = move_files_to_empty_space(udisk)

    # print(f"{files=}\n{fileid}\n{freespace=}\n{udisk=}")
    # print(f"{''.join(flatten_disk(udisk))}")
    print(f"{''.join(flatten_disk(sdisk))}")

    total = checksum(flatten_disk(sdisk))

    return total


if __name__ == "__main__":
    if unittest.main(exit=False).result.wasSuccessful():
        file_content = None
        with open("input.txt") as infile:
            file_content = infile.read()

        file_content = file_content[:-1]
        output = process(file_content)
        print(f"Ans: {output}")
