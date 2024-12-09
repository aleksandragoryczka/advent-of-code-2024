with open('inputs/day06/input.txt') as f:
    lines = f.readlines()

lines = [list(line) for line in lines]

row_len = len(lines[0]) - 1
column_len = len(lines)
fields_set = set()

i_position = 0
j_position = 0
for i in range(column_len):
    for j in range(row_len):
        if lines[i][j] == "^":
            i_position = i
            j_position = j
            fields_set.add((i, j))

def find_obstacle_up(i_position: int, j_position: int) -> tuple:
    for i in range(i_position - 1, -1, -1):
        if lines[i][j_position] == "#":
            return i + 1, j_position
        fields_set.add((i, j_position))
    return 0, j_position

def find_obstacle_right(i_position: int, j_position: int) -> tuple:
    for j in range(j_position + 1, row_len):
        if lines[i_position][j] == "#":
            return i_position, j - 1
        fields_set.add((i_position, j))
    return i_position, row_len

def find_obstacle_down(i_position: int, j_position: int) -> tuple:
    for i in range(i_position + 1, column_len):
        if lines[i][j_position] == "#":
            return i - 1, j_position
        fields_set.add((i, j_position))
    return column_len, j_position

def find_obstacle_left(i_position: int, j_position: int) -> tuple:
    for j in range(j_position - 1, -1, -1):
        if lines[i_position][j] == "#":
            return i_position, j + 1
        fields_set.add((i_position, j))
    return i_position, 0

def check_if_left(i: int, j: int) -> bool:
    if i_position == 0 or i_position == column_len or j_position == 0 or j_position == row_len:
        return True
    return False


while True:
    i_position, j_position = find_obstacle_up(i_position, j_position)
    if check_if_left(i_position, j_position):
        break
    i_position, j_position = find_obstacle_right(i_position, j_position)
    if check_if_left(i_position, j_position):
        break
    i_position, j_position = find_obstacle_down(i_position, j_position)
    if check_if_left(i_position, j_position):
        break
    i_position, j_position = find_obstacle_left(i_position, j_position)
    if check_if_left(i_position, j_position):
        break
        

print(len(fields_set))