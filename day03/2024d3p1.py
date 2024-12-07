import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

m = re.compile(pattern)
infile = ""
with open("day3.in") as inf:
    infile = inf.read()

fnd = m.findall(infile)

ans = sum([int(x) * int(y) for x, y in fnd])

print(ans)
