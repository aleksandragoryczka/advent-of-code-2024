with open('inputs/day02/input.txt') as f:
    lines = f.readlines()

def check_line(line: list) -> bool:
    for i in range(len(line) - 1):
        diff = abs(line[i] - line[i+1])
        if diff > 3 or diff < 1:
            return False
    return True

safe_reports = 0
for line in lines:
    splitted_line = line.split()
    splitted_line = [int(val) for val in splitted_line]

    if sorted(splitted_line) == splitted_line or sorted(splitted_line, reverse=True) == splitted_line:
        if check_line(splitted_line):
            safe_reports += 1

print(safe_reports)
