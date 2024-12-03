# https://adventofcode.com/2024/day/3

import re
from functools import reduce
from operator import mul

# parse input

with open("input.txt", "r") as input_file:
    corrupted_program = input_file.read().strip()


# part 1

muls = re.findall(r"mul\(\d+\,\d+\)", corrupted_program)

sum_of_muls = sum([a * b for a, b in [map(int, re.findall(r"\d+", mul)) for mul in muls]])

print(f"The sum of the muls is {sum_of_muls}")


# part 2

instructions = re.findall(
    r"""(
        mul\(\d+\,\d+\) |
        do\(\) |
        don\'t\(\)
    )""",
    corrupted_program,
    re.VERBOSE,
)
do = True
sum = 0
for instruction in instructions:
    if do and instruction.startswith("mul"):
        sum += reduce(mul, map(int, re.findall(r"\d+", instruction)))
    else:
        do = True if instruction == "do()" else False

print(f"The sum of the muls with enable and disable instruction is {sum}")
