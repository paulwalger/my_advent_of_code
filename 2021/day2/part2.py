"""
In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0.
The commands also mean something entirely different than you first thought:

    - down X increases your aim by X units.
    - up X decreases your aim by X units.
    - forward X does two things:
        > It increases your horizontal position by X units.
        > It increases your depth by your aim multiplied by X.
"""

with open("input.txt", "r") as input_file:
    instructions = [line.rstrip().split(" ") for line in input_file]
    instructions = [(i[0], int(i[1])) for i in instructions]

    horizontal = 0
    depth = 0
    aim = 0

    for name, value in instructions:
        if name == "up":
            aim -= value
        elif name == "down":
            aim += value
        elif name == "forward":
            horizontal += value
            depth += aim * value

    print(horizontal, depth)
    print(horizontal * depth)
