# https://adventofcode.com/2024/day/8


# parse input


import itertools
from collections import defaultdict

with open("2024/day_08/input.txt", "r") as input_file:
    map = [row.strip() for row in input_file]
    size = len(map)

# part 1


def is_in_map(x, y):
    return 0 <= x < size and 0 <= y < size


antenna_locations_by_frequencies = defaultdict(list)
antinodes = set()

for x in range(size):
    for y in range(size):
        if map[x][y] != ".":
            antenna_locations_by_frequencies[map[x][y]].append((x, y))

for freq, locations in antenna_locations_by_frequencies.items():
    for loc_a, loc_b in itertools.combinations(locations, 2):
        dx, dy = loc_a[0] - loc_b[0], loc_a[1] - loc_b[1]
        antinode_a = (loc_a[0] + dx, loc_a[1] + dy)
        antinode_b = (loc_b[0] - dx, loc_b[1] - dy)
        if is_in_map(*antinode_a):
            antinodes.add(antinode_a)
        if is_in_map(*antinode_b):
            antinodes.add(antinode_b)

print(f"Number of antinodes: {len(antinodes)}")


# part 2

antinodes = set()

for freq, locations in antenna_locations_by_frequencies.items():
    for loc_a, loc_b in itertools.combinations(locations, 2):
        dx, dy = loc_a[0] - loc_b[0], loc_a[1] - loc_b[1]

        x, y = loc_a
        while is_in_map(x, y):
            antinodes.add((x, y))
            x, y = x + dx, y + dy

        x, y = loc_b
        while is_in_map(x, y):
            antinodes.add((x, y))
            x, y = x - dx, y - dy

print(f"Number of antinodes: {len(antinodes)}")
