# https://adventofcode.com/2024/day/6


# parse input


with open("2024/day_06/input.txt", "r") as input_file:
    map = [list(row.strip()) for row in input_file.readlines()]


# part 1


def get_intial_guard_pos(map):
    for x in range(len(map)):
        for y in range(len(map)):
            if map[x][y] in {">", "<", "^", "v"}:
                return x, y


def next_guard_pos_and_direction(map, x, y, direction):
    match direction:
        case ">":
            if y + 1 < len(map) and map[x][y + 1] == "#":
                return x, y, "v"
            return x, y + 1, direction
        case "<":
            if y - 1 >= 0 and map[x][y - 1] == "#":
                return x, y, "^"
            return x, y - 1, direction
        case "^":
            if x - 1 >= 0 and map[x - 1][y] == "#":
                return x, y, ">"
            return x - 1, y, direction
        case "v":
            if x + 1 < len(map) and map[x + 1][y] == "#":
                return x, y, "<"
            return x + 1, y, direction


x, y = get_intial_guard_pos(map)
direction = map[x][y]
disctint_pos = set()

while (0 <= x < len(map)) and (0 <= y < len(map)):
    disctint_pos.add((x, y))
    x, y, direction = next_guard_pos_and_direction(map, x, y, direction)

print(f"Number of distinct positions: {len(disctint_pos)}")

# part 2


def is_stuck(map):
    disctint_pos = set()
    x, y = get_intial_guard_pos(map)
    direction = map[x][y]
    while (0 <= x < len(map)) and (0 <= y < len(map)):
        disctint_pos.add((x, y, direction))
        x, y, direction = next_guard_pos_and_direction(map, x, y, direction)
        if (x, y, direction) in disctint_pos:
            return 1
    return 0


nb_stuck = 0

for obs_x in range(len(map)):
    for obs_y in range(len(map)):
        if map[obs_x][obs_y] in {">", "<", "^", "v", "#"}:
            continue

        map[obs_x][obs_y] = "#"
        nb_stuck += is_stuck(map)
        map[obs_x][obs_y] = "."

print(f"Number of different obstruction position: {nb_stuck}")
