import itertools

with open('inputs/day07/input.txt') as f:
    lines = f.readlines()

sum = 0

def create_calculations(first_list: list, second_list: list) -> list:
    third_list = [None] * (len(first_list) + len(second_list))
    third_list[::2] = first_list
    third_list[1::2] = second_list
    return third_list

def make_calculation(calculation: list) -> int:
    while len(calculation) > 1:
        result = eval("".join(calculation[0:3]))
        calculation.pop(0)
        calculation.pop(0)
        calculation[0] = str(result)
    return int(calculation[0])


for line in lines:
    result = line.split(":")[0]
    elements = line.split(":")[1].split()
    operators_permutations = list(itertools.product("+*", repeat=len(elements) - 1))
    for permutation in operators_permutations:
        calculation_created = create_calculations(elements, permutation)
        calculation_made = make_calculation(calculation_created)
        if int(result) == calculation_made:
            sum += calculation_made
            break
        
print(sum)