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


line = [int(x) for x in list(line)]
if len(line) % 2 == 0:
    line_reverted = line[-2::-2]
else:
    line_reverted = line[::-2]
line_reverted_length = len(line_reverted)

new_system = blocks.copy()

def find_sub_list(sublist: list, list: list) -> tuple:
    sublist2=len(sublist)
    for ind in (i for i, e in enumerate(list) if e==sublist[0]):
        if list[ind:ind+sublist2]==sublist:
            return ind, ind+sublist2-1
    return -1, -1

for idx, val in enumerate(line_reverted):    
    if val != 0:
        result_found = find_sub_list(["." for _ in range(val)], new_system)[0]
        searching_value = line_reverted_length - idx - 1
        try:
            current_num_index = blocks.index(str(searching_value))
        except ValueError:
            continue
        if result_found > -1 and result_found < current_num_index:
            for i in range(val):
                new_system[result_found + i] = blocks[current_num_index + i]
                new_system[current_num_index + i] = "."

checksum = 0

for idx, val in enumerate(new_system):
    if val == ".":
        continue
    checksum += idx * int(val)

print(checksum)