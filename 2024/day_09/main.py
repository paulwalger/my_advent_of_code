# https://adventofcode.com/2024/day/8


# parse input


with open("2024/day_09/input.txt", "r") as input_file:
    disk_map = list(map(int, input_file.read().strip()))


# part 1


def disk_map_to_blocks(disk_map):
    expanded = []
    for idx, value in enumerate(disk_map):
        if idx % 2 == 0:  # file
            expanded += [idx // 2] * value
        else:  # free space
            expanded += ["."] * value
    return expanded


disk_block = disk_map_to_blocks(disk_map)
size = sum(disk_map)

left_free_block_idx = disk_map[0]
total_free_block = sum(nb_block for nb_block in disk_map[1::2])
end_file_block_idx = size - 1

while (size - total_free_block) >= left_free_block_idx:  # while all free block not at the end
    # find the last file block
    while disk_block[end_file_block_idx] == ".":
        end_file_block_idx -= 1

    # find the next free block
    while disk_block[left_free_block_idx] != ".":
        left_free_block_idx += 1

    if left_free_block_idx >= end_file_block_idx:
        break

    # exchange the last file block with the first free block
    disk_block[left_free_block_idx], disk_block[end_file_block_idx] = (
        disk_block[end_file_block_idx],
        disk_block[left_free_block_idx],
    )


checksum = sum([value * idx for idx, value in enumerate(disk_block) if value != "."])

print(f"checksum: {checksum}")

# part 2

# start by finding the free and file blocks
free_blocks, file_blocks = [], []
start_block_idx = 0
for idx, nb_block in enumerate(disk_map):
    if idx % 2 != 0:
        free_blocks.append([start_block_idx, nb_block])
    else:
        file_blocks.append([start_block_idx, nb_block])
    start_block_idx += nb_block

disk_block = disk_map_to_blocks(disk_map)

for file_block_idx, file_nb_block in reversed(file_blocks):
    k = 0

    # find the first free block idx that can contain the file block
    while k < len(free_blocks) and free_blocks[k][1] < file_nb_block:
        k += 1

    # no free block available on left side
    if k == len(free_blocks) or free_blocks[k][0] > file_block_idx:
        continue

    # exchange the file block with the free block
    (
        disk_block[free_blocks[k][0] : free_blocks[k][0] + file_nb_block],
        disk_block[file_block_idx : file_block_idx + file_nb_block],
    ) = disk_block[file_block_idx : file_block_idx + file_nb_block], ["."] * file_nb_block

    # update free blocks config
    free_blocks[k][0] += file_nb_block
    free_blocks[k][1] -= file_nb_block

checksum = sum([value * idx for idx, value in enumerate(disk_block) if value != "."])
print(f"checksum: {checksum}")
