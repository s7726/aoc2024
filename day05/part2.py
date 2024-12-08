import unittest
import re
import random
from functools import cmp_to_key
from collections import defaultdict


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

        out = 123

        self.assertEqual(process(test_in), out)

    def test_middle_number(self):
        samp = [[75, 47, 61, 53, 29], [97, 61, 53, 29, 13], [75, 29, 13]]

        self.assertEqual(middle_number(samp[0]), 61)
        self.assertEqual(middle_number(samp[1]), 53)
        self.assertEqual(middle_number(samp[2]), 29)


def middle_number(l) -> int:
    if len(l) == 0:
        return 0
    return l[int(len(l) / 2)]


def passes_rules(rules, pages):
    passes = False
    for i, page in enumerate(pages):
        try:
            rule = rules[page]

        except KeyError:
            continue

        passes = all([p not in rule for p in pages[:i]])
        if not passes:
            return False

    return passes


def passes_rules_list(rules, pages):
    passes = {}
    for i, page in enumerate(pages):
        try:
            rule = rules[page]

        except KeyError:
            passes[i] = None
            continue

        passes[i] = [p not in rule for p in pages[:i]]

    return passes


def sort_on_rules(rules):
    rules = rules

    def sort_pages(a, b):
        if b in rules[a]:
            return -1
        return 1

    return sort_pages


def make_failing_pass(rules, pages):
    return sorted(pages, key=cmp_to_key(sort_on_rules(rules)))


def process(input):
    total: int = 0

    raw_rules = re.findall(r"^(\d+)\|(\d+)$", input, re.MULTILINE)
    raw_numbers = [
        p.split(",") for p in re.findall(r"^\d+(?:,\d+)+", input, re.MULTILINE)
    ]

    page_numbers = [[int(p) for p in l] for l in raw_numbers]

    rules = defaultdict(list)

    for f_, s_ in raw_rules:
        first = int(f_)
        second = int(s_)
        try:
            rules[first]
        except KeyError:
            rules[first] = []
        rules[first].append(second)

    passes = []
    fails = []

    for pages in page_numbers:
        if passes_rules(rules, pages):
            passes.append(pages)
        else:
            fails.append(pages)

    print(f"Failing: {len(fails)}")

    fixed_fails = []

    for i, f in enumerate(fails):
        fixed_fails.append(make_failing_pass(rules, f))
        print(f"{i/len(fails):>6.1%}", end="\r")

    for line in fixed_fails:
        total += middle_number(line)

    return total


if __name__ == "__main__":
    if unittest.main(exit=False).result.wasSuccessful():
        file_content = None
        with open("input.txt") as infile:
            file_content = infile.read()
        output = process(file_content)
        print(f"Ans: {output}")
