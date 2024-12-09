with open('inputs/day09/input.txt') as f:
    line = f.read()

blocks = []

counter = 0
for idx, num in enumerate(line):
    if idx % 2 == 0:
        [blocks.append(str(counter)) for _ in range(int(num))]
        counter += 1
    else:
        [blocks.append(".") for _ in range(int(num))]

for idx, val in enumerate(blocks):
    if val == ".":
        while blocks[-1] == ".":
            blocks.pop()
        blocks[idx] = blocks.pop()

checksum = 0
for idx, val in enumerate(blocks):
    checksum += idx * int(val)

print(checksum)