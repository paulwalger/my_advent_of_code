# https://adventofcode.com/2024/day/7


# parse input


import itertools

with open("2024/day_07/input.txt", "r") as input_file:
    rows = [row.strip() for row in input_file]
    equations = []
    for row in rows:
        value, numbers = row.split(":")
        numbers = list(map(int, numbers.strip().split(" ")))
        equations.append((value, numbers))

# part 1


def can_equation_be_true(equation, set_operators="+*"):
    value, numbers = equation
    size = len(numbers)
    for operators in itertools.product(set_operators, repeat=size - 1):
        test_value = numbers[0]
        for idx, op in enumerate(operators):
            if op in "+*":
                test_value = eval(f"{test_value} {op} {numbers[idx+1]}")
            else:
                test_value = int(f"{test_value}{numbers[idx+1]}")
            if test_value > int(value):
                break
        if test_value == int(value):
            return True
    return False


sum_true_equation = sum([int(equation[0]) for equation in equations if can_equation_be_true(equation, "+*")])

print(f"Sum of test value of equations that can be true: {sum_true_equation}")

# part 2

sum_true_equation = sum([int(equation[0]) for equation in equations if can_equation_be_true(equation, "+*|")])

print(f"Sum of test value of equations with concatenation operator that can be true: {sum_true_equation}")
