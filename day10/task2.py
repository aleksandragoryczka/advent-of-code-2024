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
def find_recursively_next_element(el: int, i: int, j: int) -> int:
    if el == 9:
        return 1
    search = 0
    if i+1 <= len(board) - 1 and board[i+1][j] == el + 1:
        search += find_recursively_next_element(el+1, i+1, j)
    if j+1 <= len(board[0]) - 1 and board[i][j+1] == el + 1:
        search += find_recursively_next_element(el+1, i, j+1)
    if i-1 >= 0 and board[i-1][j] == el + 1:
        search += find_recursively_next_element(el+1, i-1, j)
    if j-1 >= 0 and board[i][j-1] == el + 1:
        search += find_recursively_next_element(el+1, i, j-1)
    return search

sum = 0
counter = 1
for i, row in enumerate(board):
    for j, el in enumerate(row):
        if el == 0:
            sum += find_recursively_next_element(0, i, j)

print(sum)


