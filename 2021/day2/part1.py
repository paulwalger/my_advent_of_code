"""
Calculate the horizontal position and depth you would have after following the planned course.
What do you get if you multiply your final horizontal position by your final depth?
"""

with open("input.txt", "r") as input_file:
    instructions = [line.rstrip().split(" ") for line in input_file]
    instructions = [(i[0], int(i[1])) for i in instructions]

    horizontal = 0
    depth = 0

    for name, value in instructions:
        if name == "up":
            depth -= value
        elif name == "down":
            depth += value
        elif name == "forward":
            horizontal += value

    print(horizontal, depth)
    print(horizontal * depth)
