class Cave:
    def __init__(self, name: str) -> None:
        self.name = name
        self.connections = []

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, __o: object) -> bool:
        return self.name == __o.name

    def __hash__(self) -> int:
        return hash(self.name)

    @property
    def is_small(self) -> bool:
        return self.name.islower()

    @property
    def is_start(self) -> bool:
        return self.name == "start"

    @property
    def is_end(self) -> bool:
        return self.name == "end"

    @property
    def to_caves(self):
        return filter(lambda x: not x.is_start, self.connections)


def get_input_caves(file_name):
    caves = {}
    with open(file_name, "r") as input_file:
        for line in input_file:
            from_cave, to_cave = [Cave(name) for name in line.strip().split("-")]
            if from_cave.name not in caves:
                caves[from_cave.name] = from_cave
            if to_cave.name not in caves:
                caves[to_cave.name] = to_cave
            caves[from_cave.name].connections.append(caves[to_cave.name])
            caves[to_cave.name].connections.append(caves[from_cave.name])
    return caves


def count_paths(path, quota_reached=False):
    current_cave = path[-1]

    if current_cave.is_end:
        return 1

    # generate a new path with all posibilities not already explored
    count = 0
    for next_cave in current_cave.to_caves:
        if next_cave.is_small and next_cave in path and quota_reached:
            pass
        else:
            new_quota_reached = quota_reached
            if next_cave.is_small and not quota_reached and next_cave in path:
                new_quota_reached = True
            new_path = [*path, next_cave]
            count += count_paths(new_path, new_quota_reached)

    return count


def get_count_unique_paths(caves):
    start = caves["start"]
    count = count_paths([start], quota_reached=True)
    return count


def get_count_unique_paths_with_quota(caves):
    start = caves["start"]
    count = count_paths([start])
    return count


caves = get_input_caves("input.txt")

print(f"Number of unique paths: {get_count_unique_paths(caves)}")

print(f"Number of unique paths with quota: {get_count_unique_paths_with_quota(caves)}")
