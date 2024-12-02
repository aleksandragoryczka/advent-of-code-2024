with open('inputs/day02/input.txt') as f:
    lines = f.readlines()

def check_line(line: list) -> bool:
    for i in range(len(line) - 1):
        diff = abs(line[i] - line[i+1])
        if diff > 3 or diff < 1:
            return False
    return True

def try_remove_one_element(line: list) -> int:
    for i in range(len(line)):
        line_copy = line.copy()
        line_copy.pop(i)
        if (sorted(line_copy) == line_copy or sorted(line_copy, reverse=True) == line_copy) and check_line(line_copy):
            return 1
    return 0

safe_reports = 0
for line in lines:
    splitted_line = line.split()
    splitted_line = [int(val) for val in splitted_line]

    if sorted(splitted_line) == splitted_line or sorted(splitted_line, reverse=True) == splitted_line:
        if check_line(splitted_line):
            safe_reports += 1
        else:
            safe_reports += try_remove_one_element(splitted_line)
    else:
        safe_reports += try_remove_one_element(splitted_line)

print(safe_reports)
