import os

day_nr = '01'

os.mkdir(f"day{day_nr}")
open(f"day{day_nr}/task1.py", "w")
open(f"day{day_nr}/task2.py", "w")

os.mkdir(f"inputs/day{day_nr}")
open(f"inputs/day{day_nr}/test.txt", "w")
open(f"inputs/day{day_nr}/input.txt", "w")
