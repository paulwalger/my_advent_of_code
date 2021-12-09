from functools import reduce


def get_heightmap():
    with open("input.txt", "r") as input_file:
        heightmap = []
        for line in input_file:
            heightmap.append(list(map(int, list(line.strip()))))
        return heightmap


def get_adjacent_coords(x, y, heightmap):
    width = len(heightmap[0])
    height = len(heightmap)
    adjacent_coords = []
    for x_off, y_off in {(-1, 0), (1, 0), (0, -1), (0, 1)}:
        if x + x_off >= 0 and x + x_off < width and y + y_off >= 0 and y + y_off < height:
            adjacent_coords.append((x + x_off, y + y_off))
    return adjacent_coords


def get_low_points(heightmap):
    low_points = []
    width = len(heightmap[0])
    height = len(heightmap)
    for x in range(width):
        for y in range(height):
            adj_values = [heightmap[adj_x][adj_y] for adj_x, adj_y in get_adjacent_coords(x, y, heightmap)]
            if heightmap[x][y] < min(adj_values):
                low_points.append((x, y))
    return low_points


def get_risk_level(heightmap):
    low_points = get_low_points(heightmap)
    return sum(heightmap[x][y] for x, y in low_points) + len(low_points)


def get_size_bassin(x, y, heightmap, visited):
    if heightmap[x][y] == 9 or (x, y) in visited:
        return 0
    visited.add((x, y))
    return 1 + sum(
        get_size_bassin(adj_x, adj_y, heightmap, visited) for adj_x, adj_y in get_adjacent_coords(x, y, heightmap)
    )


def get_mult_bigest_size_bassins(heightmap):
    visited = set()
    size_bassins = set()
    for low_point in get_low_points(heightmap):
        if low_point not in visited:
            size = get_size_bassin(*low_point, heightmap, visited)
            size_bassins.add(size)
            if len(size_bassins) > 3:
                size_bassins.remove(min(size_bassins))
    return reduce(lambda a, b: a * b, size_bassins)


heightmap = get_heightmap()
print(f"Part 1: Risk level: {get_risk_level(heightmap)}")
print(f"Part 2: Multiplication of the 3 biggest bassins: {get_mult_bigest_size_bassins(heightmap)}")
