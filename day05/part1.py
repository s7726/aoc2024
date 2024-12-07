import unittest
import re


class TestPart(unittest.TestCase):
    def test_example(self):
        test_in = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

        out = 143

        self.assertEqual(process(test_in), out)

    def test_middle_number(self):
        samp = [[75, 47, 61, 53, 29], [97, 61, 53, 29, 13], [75, 29, 13]]

        self.assertEqual(middle_number(samp[0]), 61)
        self.assertEqual(middle_number(samp[1]), 53)
        self.assertEqual(middle_number(samp[2]), 29)


def middle_number(l):
    return l[int(len(l) / 2)]


def passes_rules(rules, pages):
    print(f"{rules=}")
    print(f"{pages=}")
    passes = False
    for i, page in enumerate(pages):
        try:
            rule = rules[page]

        except KeyError:
            print(f"{i}:{page} not found")
            continue

        passes = all([p not in rule for p in pages[:i]])
        if not passes:
            return False

        print(f"{page}:{passes=}")

    return passes


def process(input):
    total = 0

    raw_rules = re.findall(r"^(\d+)\|(\d+)$", input, re.MULTILINE)
    raw_numbers = [
        p.split(",") for p in re.findall(r"^\d+(?:,\d+)+", input, re.MULTILINE)
    ]

    page_numbers = [[int(p) for p in l] for l in raw_numbers]

    rules = {}

    for f_, s_ in raw_rules:
        first = int(f_)
        second = int(s_)
        try:
            rules[first]
        except KeyError:
            rules[first] = []
        rules[first].append(second)

    passes = []

    for pages in page_numbers:
        if passes_rules(rules, pages):
            passes.append(pages)
            print("PASSED")

    for line in passes:
        total += middle_number(line)

    return total


if __name__ == "__main__":
    if unittest.main(exit=False).result.wasSuccessful():
        file_content = None
        with open("input.txt") as infile:
            file_content = infile.read()
        output = process(file_content)
        print(f"Ans: {output}")
