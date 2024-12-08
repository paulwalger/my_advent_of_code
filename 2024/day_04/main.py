# https://adventofcode.com/2024/day/4

import re

# parse input

with open("2024/day_04/input.txt", "r") as input_file:
    grid = [row.strip() for row in input_file.readlines()]


# part 1


def generate_all_rows(grid):
    size = len(grid)

    # horizontal
    rows = [row for row in grid]

    # vertical
    rows += ["".join([grid[x][y] for x in range(size)]) for y in range(size)]

    # diagonal
    for start_y in range(size):
        for start_x in (0, size - 1):  # start from top row or bottom row
            if start_x == size - 1 and start_y in [0, size - 1]:
                continue  # already counted

            r_diag = ""  # diagonal from top left to bottom right
            x, y = start_x, start_y
            while (0 <= x < size) and (0 <= y < size):
                r_diag += grid[x][y]
                x = x + 1 if start_x == 0 else x - 1
                y = y + 1 if start_x == 0 else y - 1
            rows.append(r_diag)

            l_diag = ""  # diagonal from top right to bottom left
            x, y = start_x, start_y
            while (0 <= x < size) and (0 <= y < size):
                l_diag += grid[x][y]
                x = x + 1 if start_x == 0 else x - 1
                y = y - 1 if start_x == 0 else y + 1

            rows.append(l_diag)

    return rows


nb_xmas = sum(len(re.findall(r"XMAS", row)) + len(re.findall(r"SAMX", row)) for row in generate_all_rows(grid))

print(f"Number of XMAS {nb_xmas}")


# part 2

size = len(grid)


def is_x_mas(grid, x, y):
    diag_1 = grid[x - 1][y - 1] + grid[x + 1][y + 1]
    diag_2 = grid[x - 1][y + 1] + grid[x + 1][y - 1]
    return diag_1 in {"MS", "SM"} and diag_2 in {"MS", "SM"}


sum = 0
for x in range(1, size - 1):
    for y in range(1, size - 1):
        if grid[x][y] == "A" and is_x_mas(grid, x, y):
            sum += 1

print(f"Number of X-MAS {sum}")
