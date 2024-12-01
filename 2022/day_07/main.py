from pathlib import Path


def move_to_new_dir(current_dir: Path, cd_dir):
    if cd_dir == "/":
        current_dir = Path("/")
    elif cd_dir == "..":
        current_dir = current_dir.parent
    else:
        current_dir = current_dir / cd_dir
    return current_dir


def recursive_total_size(dir: Path, size_by_dir: dict):
    return size_by_dir[dir]["size"] + sum(
        [recursive_total_size(sub_dir, size_by_dir) for sub_dir in size_by_dir[dir]["sub_dirs"]]
    )


def main():
    size_by_dir = {}
    current_dir = None
    with open("input.txt", "r") as input_file:
        for line in input_file:
            line = line.strip()
            if line.startswith("$ cd"):
                current_dir = move_to_new_dir(current_dir, line.split()[-1])
                if current_dir not in size_by_dir:
                    size_by_dir[current_dir] = {"size": 0, "visited": 0, "sub_dirs": []}
            elif line.startswith("$ ls"):
                size_by_dir[current_dir]["visited"] += 1
            elif line.startswith("dir"):
                if size_by_dir[current_dir]["visited"] == 1:
                    sub_dir = line.split()[1]
                    size_by_dir[current_dir]["sub_dirs"].append(current_dir / sub_dir)
            else:
                if size_by_dir[current_dir]["visited"] == 1:
                    size = int(line.split()[0])
                    size_by_dir[current_dir]["size"] += size

    # part1
    sum_part1 = sum(
        [size for size in [recursive_total_size(dir, size_by_dir) for dir in size_by_dir.keys()] if size <= 100000]
    )
    print(
        "Find all of the directories with a total size of at most 100000. "
        "What is the sum of the total sizes of those directories? ",
        sum_part1,
    )

    # part2
    SPACE_AVAILABLE = 70000000
    NEEDED_UNUSED_SPACE = 30000000

    total_space_used = sum([dir["size"] for dir in size_by_dir.values()])
    current_unused_space = SPACE_AVAILABLE - total_space_used

    minimum_delete = NEEDED_UNUSED_SPACE - current_unused_space

    print(
        "part2 ",
        min(
            [
                size
                for size in [recursive_total_size(dir, size_by_dir) for dir in size_by_dir.keys()]
                if size >= minimum_delete
            ]
        ),
    )


if __name__ == "__main__":
    main()
