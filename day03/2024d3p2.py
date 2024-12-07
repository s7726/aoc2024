import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)|(d)o\(\)|do(n)\'t\(\)"

m = re.compile(pattern)
infile = ""
with open("day3.in") as inf:
    infile = inf.read()

fnd = m.findall(infile)

en = True
dos = []

for s in fnd:
    if s[3] == "n":
        en = False
    if s[2] == "d":
        en = True
    if en and len(s[0]):
        dos.append(s[:2])


ans = sum([int(x) * int(y) for x, y in dos])

print(ans)
