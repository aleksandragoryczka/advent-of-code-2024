with open('inputs/day06/input.txt') as f:
    lines = f.readlines()

lines = [list(line) for line in lines]

row_len = len(lines[0]) - 1
column_len = len(lines)
cycles_found = 0

i_init_position = 0
j_init_position = 0
for i in range(column_len):
    for j in range(row_len):
        if lines[i][j] == "^":
            i_init_position = i
            j_init_position = j

def find_obstacle_up(i_position: int, j_position: int) -> tuple:
    for i in range(i_position - 1, -1, -1):
        if lines[i][j_position] == "#":
            return i + 1, j_position
    return 0, j_position

def find_obstacle_right(i_position: int, j_position: int) -> tuple:
    for j in range(j_position + 1, row_len):
        if lines[i_position][j] == "#":
            return i_position, j - 1
    return i_position, row_len

def find_obstacle_down(i_position: int, j_position: int) -> tuple:
    for i in range(i_position + 1, column_len):
        if lines[i][j_position] == "#":
            return i - 1, j_position
    return column_len, j_position

def find_obstacle_left(i_position: int, j_position: int) -> tuple:
    for j in range(j_position - 1, -1, -1):
        if lines[i_position][j] == "#":
            return i_position, j + 1
    return i_position, 0

def check_if_left(i: int, j: int) -> bool:
    if i == 0 or i == column_len or j == 0 or j == row_len:
        return True
    return False

def solve() -> bool:
    iterations = 0
    i_position = i_init_position
    j_position = j_init_position
    while True:
        if iterations >= row_len*column_len*4 + 1:
            return True
        iterations += 1
        i_position, j_position = find_obstacle_up(i_position, j_position)
        if check_if_left(i_position, j_position):
            return False
        iterations += 1
        i_position, j_position = find_obstacle_right(i_position, j_position)
        if check_if_left(i_position, j_position):
            return False
        iterations += 1
        i_position, j_position = find_obstacle_down(i_position, j_position)
        if check_if_left(i_position, j_position):
            return False
        iterations += 1
        i_position, j_position = find_obstacle_left(i_position, j_position)
        if check_if_left(i_position, j_position):
            return False

for i in range(column_len):
    for j in range(row_len):
        if lines[i][j] in [".", "^"]:
            lines[i][j] = "#"
            if solve():
                cycles_found += 1
            lines[i][j] = "."

print(cycles_found)