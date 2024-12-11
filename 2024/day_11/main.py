# https://adventofcode.com/2024/day/11

import functools

# parse input


with open("2024/day_11/input.txt", "r") as input_file:
    stones = list(map(int, input_file.read().strip().split(" ")))

# part 1


@functools.cache
def blink_at_stone(stone: int):
    if stone == 0:
        return [1]
    if len(str(stone)) % 2 == 0:
        return [
            int(str(stone)[: len(str(stone)) // 2]),
            int(str(stone)[len(str(stone)) // 2 :].lstrip("0") or "0"),
        ]
    return [stone * 2024]


@functools.cache
def count_stone_after_x_blinks_at_given_stone_rec(stone_int: int, nb_blinks: int):
    if nb_blinks == 0:
        return 1
    return sum(
        [
            count_stone_after_x_blinks_at_given_stone_rec(new_stone, nb_blinks - 1)
            for new_stone in blink_at_stone(stone_int)
        ]
    )


nb_stones = sum([count_stone_after_x_blinks_at_given_stone_rec(stone, 25) for stone in stones])

print(f"Number of stones after 25 blinks: {nb_stones}")


# part 2

nb_stones = sum([count_stone_after_x_blinks_at_given_stone_rec(stone, 75) for stone in stones])

print(f"Number of stones after 75 blinks: {nb_stones}")
