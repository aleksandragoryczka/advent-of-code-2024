with open('inputs/day01/input.txt') as f:
    lines = f.readlines()

first_column = []
second_column = []
for line in lines:
    splitted_line = line.split()
    first_column.append(int(splitted_line[0]))
    second_column.append(int(splitted_line[1]))

first_column_sorted = sorted(first_column)
second_column_sroted = sorted(second_column)

sum = 0
for i in range(len(first_column_sorted)):
    sum += abs(first_column_sorted[i] - second_column_sroted[i])

print(sum)