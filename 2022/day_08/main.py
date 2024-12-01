def is_visible(forest, x, y) -> bool:
    """Return True if the Tree in position x, y is visible from at least one side"""
    # EDGE
    if x == 0 or x == len(forest) - 1 or y == 0 or y == len(forest[0]) - 1:
        return True
    tree_height = forest[x][y]
    # NORTH:
    if all([forest[x - k][y] < tree_height for k in range(1, x + 1)]):
        return True
    # EAST
    elif all([forest[x][y + k] < tree_height for k in range(1, len(forest[0]) - y)]):
        return True
    # SOUTH
    elif all([forest[x + k][y] < tree_height for k in range(1, len(forest) - x)]):
        return True
    # WEST
    elif all([forest[x][y - k] < tree_height for k in range(1, y + 1)]):
        return True
    return False


def distance(height, trees_in_direction):
    """
    return distance to the first tree in a direction that is same height or taller.
    the limit is the edge.
    """
    distance = 0
    for tree in trees_in_direction:
        distance += 1
        if tree >= height:
            break
    return distance


def scenic_score(forest, x, y):
    # edge
    if x == 0 or x == len(forest) - 1 or y == 0 or y == len(forest[0]) - 1:
        return 0
    # NORTH
    north_trees = [forest[x - k][y] for k in range(1, x + 1)]
    # EAST
    east_trees = [forest[x][y + k] for k in range(1, len(forest[0]) - y)]
    # SOUTH
    south_trees = [forest[x + k][y] for k in range(1, len(forest) - x)]
    # WEST:
    west_trees = [forest[x][y - k] for k in range(1, y + 1)]

    height = forest[x][y]
    return (
        distance(height, north_trees)
        * distance(height, east_trees)
        * distance(height, south_trees)
        * distance(height, west_trees)
    )


def main():
    with open("input.txt", "r") as input_file:
        forest = [list(map(int, list(line.strip()))) for line in input_file]

        print(sum(is_visible(forest, x, y) for y in range(len(forest[0])) for x in range(len(forest))))

        print(max(scenic_score(forest, x, y) for y in range(len(forest[0])) for x in range(len(forest))))


if __name__ == "__main__":
    main()
