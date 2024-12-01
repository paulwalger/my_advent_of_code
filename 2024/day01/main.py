# https://adventofcode.com/2024/day/1

from typing import Counter

# parse input

with open("input.txt", "r") as input_file:
    list_1, list_2 = [], []
    for row in input_file:
        a, b = map(int, row.strip().split("   "))
        list_1.append(a)
        list_2.append(b)


# part 1

total_distance = sum(abs(a - b) for a, b in zip(sorted(list_1), sorted(list_2)))

print(f"The total distance between the two lists is {total_distance}")


# part 2

counter_1 = Counter(list_1)
counter_2 = Counter(list_2)

similarity_score = sum([nb * occurence * counter_2[nb] for nb, occurence in counter_1.items()])

print(f"The similarity score between the two lists is {similarity_score}")
