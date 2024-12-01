with open('inputs/day01/input.txt') as f:
    lines = f.readlines()

first_column = []
second_column = []
for line in lines:
    splitted_line = line.split()
    first_column.append(int(splitted_line[0]))
    second_column.append(int(splitted_line[1]))

occurrences_dict = {}
sum = 0
for value in first_column:
    if value in occurrences_dict.keys():
        sum += value * occurrences_dict[value]
    else:
        occurrences = second_column.count(value)
        sum += value * occurrences
        occurrences_dict[value] = occurrences
        
print(sum)

