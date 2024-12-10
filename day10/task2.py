with open('inputs/day10/input.txt') as f:
    lines = f.readlines()

board = []
for line in lines:
    row = []
    for el in line:
        if el != "\n":
            row.append(int(el))
    board.append(row)


visited_dict = {}
def find_recursively_next_element(el: int, i: int, j: int, init_i: int, init_j: int) -> int:
    if el == 9:
        if (init_i, init_j) in visited_dict.keys():
            if (i, j) in visited_dict[(init_i, init_j)]:
                return 0
            else:
                visited_dict[(init_i, init_j)] = visited_dict[(init_i, init_j)] + [(i, j),]
        else:
            visited_dict[(init_i, init_j)] = [(i, j),]
        #board[i][j] = "."
        #print(f"i: {i} j: {j}")
        return 1
    search = 0
    if i+1 <= len(board) - 1 and board[i+1][j] == el + 1:
        #print("row down")
        search += find_recursively_next_element(el+1, i+1, j, init_i, init_j)
    if j+1 <= len(board[0]) - 1 and board[i][j+1] == el + 1:
        #print("column right")
        search += find_recursively_next_element(el+1, i, j+1, init_i, init_j)
    if i-1 >= 0 and board[i-1][j] == el + 1:
        #print("column up")
        search += find_recursively_next_element(el+1, i-1, j, init_i, init_j)
    if j-1 >= 0 and board[i][j-1] == el + 1:
        #print("column left")
        search += find_recursively_next_element(el+1, i, j-1, init_i, init_j)
    return search

sum = 0
counter = 1
for i, row in enumerate(board):
    for j, el in enumerate(row):
        if el == 0:
            sum += find_recursively_next_element(0, i, j, i, j)
#print(f"len lines: {len(lines)}")
#print(f"row len: {len(lines[0])}")
#print(board)
print(sum)


