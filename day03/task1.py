import re

with open('inputs/day03/input.txt') as f:
    line = f.read()

matches = re.findall("mul\((\d+),(\d+)\)", line)

sum = 0
for match in matches:
    sum += int(match[0]) * int(match[1])
print(sum)