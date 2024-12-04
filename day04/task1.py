with open('inputs/day04/input.txt') as f:
    lines = f.readlines()

lines = [list(line) for line in lines]

row_len = len(lines[0]) - 1
column_len = len(lines)
sum = 0

def row_check_ahead(i: int, j: int) -> int:
    if j+3 < row_len and lines[i][j+1: j+4] == ["M", "A", "S"]:
        print(f"ROW AHEAD i: {i}, j: {j}")
        return 1
    return 0

def row_check_back(i: int, j: int) -> int:
    if j-3 >= 0 and lines[i][j-3 : j] == ["S", "A", "M"]:
        print(f"ROW BACK i: {i}, j: {j}")
        return 1
    return 0

def column_check_ahead(i: int, j: int) -> int:
    if i + 3 < column_len and lines[i+1][j] == "M" and lines[i+2][j] == "A" and lines[i+3][j] == "S":
        print(f"COLUMN AHEAD i: {i}, j: {j}")
        return 1
    return 0

def column_check_back(i: int, j: int) -> int:
    if i-3 >= 0 and lines[i-1][j] == "M" and lines[i-2][j] == "A" and lines[i-3][j] == "S":
        print(f"COLUMN BACK i: {i}, j: {j}")
        return 1
    return 0

def diagonal_check_right_up(i: int, j: int) -> int:
    if i-3 >= 0 and j+3 < column_len and lines[i-1][j+1] == "M" and lines[i-2][j+2] == "A" and lines[i-3][j+3] == "S":
        print(f"DIAGONAL RIGHT UP i: {i}, j: {j}")
        return 1
    return 0

def diagonal_check_right_down(i: int, j: int) -> int:
    if i+3 < column_len and j+3 < row_len and lines[i+1][j+1] == "M" and lines[i+2][j+2] == "A" and lines[i+3][j+3] == "S":
        print(f"DIAGONAL RIGHT DOWN i: {i}, j: {j}")
        return 1
    return 0

def diagonal_check_left_up(i: int, j: int) -> int:
    if i-3 >= 0 and j-3 >= 0 and lines[i-1][j-1] == "M" and lines[i-2][j-2] == "A" and lines[i-3][j-3] == "S":
        print(f"DIAGONAL LEFT UP i: {i}, j: {j}")
        return 1
    return 0

def diagonal_check_left_down(i: int, j: int) -> int:
    if i+3 < column_len and j-3 >= 0 and lines[i+1][j-1] == "M" and lines[i+2][j-2] == "A" and lines[i+3][j-3] == "S":
        print(f"DIAGONAL LEFT DOWN i: {i}, j: {j}")
        return 1
    return 0
        
        
for i in range(column_len):
    for j in range(row_len):
        if lines[i][j] == "X":
            sum += row_check_ahead(i, j) + row_check_back(i, j) + column_check_ahead(i, j) + column_check_back(i, j) + diagonal_check_right_up(i, j) + diagonal_check_right_down(i, j) + diagonal_check_left_up(i, j) + diagonal_check_left_down(i, j)

print(sum)