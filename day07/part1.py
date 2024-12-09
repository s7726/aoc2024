import unittest
import re
from itertools import product
import operator
import copy


class TestPart(unittest.TestCase):
    def test_example(self):
        test_in = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

        out = 3749

        self.assertEqual(process(test_in), out)


OPS = ["+", "*"]
OP_DICT = {"+": operator.add, "*": operator.mul}


def operate(left, op, right):
    return OP_DICT[op](left, right)


def solve_list(vals):
    left = vals.pop(0)
    while len(vals):
        op = vals.pop(0)
        right = vals.pop(0)
        left = operate(left, op, right)
    return left


def try_ops(ans, eq):
    ops_for_each_position = list(product(OPS, repeat=len(eq) - 1))

    for opset in map(list, ops_for_each_position):
        eq_ops = eq + opset
        eq_ops[::2] = eq
        eq_ops[1::2] = opset

        if ans == solve_list(copy.copy(eq_ops)):
            return ans
    return 0


def process(input):
    total = 0

    raw_eqs = [l for l in input.splitlines()]
    eqs = []
    num_eqs = 0
    for i, item in enumerate(raw_eqs):
        if i == 674:
            pass
        ans, eq = item.split(":", 1)

        eqs.append({int(ans): list(map(int, re.findall(r"(\d+)", eq)))})
        num_eqs += 1

    print("===============================")

    print(f"eqs: {len(eqs)}/{num_eqs}/{len(raw_eqs)} => {eqs[-1]}")

    for e in eqs:
        print(f"{e.items()}")
        eq = list(e.items())
        total += try_ops(eq[0][0], eq[0][1])

    return total


if __name__ == "__main__":
    if unittest.main(exit=False).result.wasSuccessful():
        file_content = None
        with open("input.txt") as infile:
            file_content = infile.read()
        output = process(file_content)
        print(f"Ans: {output}")
