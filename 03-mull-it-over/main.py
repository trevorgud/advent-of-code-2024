import re

f = open("data.txt", "r")
mem = f.read()
# print(mem)

matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", mem)
# print(matches)

total = 0
for (x, y) in matches:
  # print(x, y)
  # Should be safe because regex enforces only numerics for these.
  total += int(x) * int(y)

print(total)
