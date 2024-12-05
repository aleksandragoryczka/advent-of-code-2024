with open('inputs/day04/input.txt') as f:
    lines = f.readlines()

lines = [list(line) for line in lines]

row_len = len(lines[0]) - 1
column_len = len(lines)
sum = 0

print(lines)

def diagonal_check_right_up(i: int, j: int) -> bool:
    if i-2 >= 0 and j+2 < column_len and lines[i-1][j+1] == "A" and lines[i-2][j+2] == "S":
        return True
    return False

def diagonal_check_right_down(i: int, j: int) -> bool:
    if i+2 < column_len and j+2 < row_len and lines[i+1][j+1] == "A" and lines[i+2][j+2] == "S":
        return True
    return False

def diagonal_check_left_up(i: int, j: int) -> bool:
    if i-2 >= 0 and j-2 >= 0 and lines[i-1][j-1] == "A" and lines[i-2][j-2] == "S":
        return True
    return False

def diagonal_check_left_down(i: int, j: int) -> bool:
    if i+2 < column_len and j-2 >= 0 and lines[i+1][j-1] == "A" and lines[i+2][j-2] == "S":
        return True
    return False
        
def check_vertical_left(i: int, j: int) -> int:
    if diagonal_check_right_down(i, j) and lines[i][j+2] == "S" and lines[i+2][j] == "M":
        return 1
    return 0

def check_vertical_right(i: int, j: int) -> int:
    if diagonal_check_left_up(i, j) and lines[i-2][j] == "M" and lines[i][j-2] == "S":
        return 1
    return 0

def check_horizontal_up(i: int, j: int) -> int:
    if diagonal_check_left_down(i, j) and lines[i+2][j] == "S" and lines[i][j-2] == "M":
        return 1
    return 0

def check_horizontal_down(i: int, j: int) -> int:
    if diagonal_check_right_up(i, j) and lines[i][j+2] == "M" and lines[i-2][j] == "S":
        return 1
    return 0


for i in range(column_len):
    for j in range(row_len):
        if lines[i][j] == "M":
            sum += check_vertical_left(i, j) + check_horizontal_down(i, j) + check_vertical_right(i, j) + check_horizontal_up(i, j)

print(sum)