from typing import List


def get_input_positions() -> List[int]:
    positions = []
    with open("input.txt", "r") as input_file:
        for line in input_file:
            positions += map(int, line.strip().split(","))
    return positions


def basic_crab_fuel_consumption(start_pos, end_pos):
    return abs(end_pos - start_pos)


def engineering_crab_fuel_consumption(start_pos, end_pos):
    n = abs(end_pos - start_pos)
    return int((n * (n + 1)) / 2)


def sum_fuel_consumption(end_pos, positions, fuel_function):
    return sum([fuel_function(crab_pos, end_pos) for crab_pos in positions])


def best_fuel_consumption(positions, fuel_function):
    min_pos, max_pos = min(positions), max(positions)
    fuel_consumptions = [
        sum_fuel_consumption(end_pos, positions, fuel_function) for end_pos in range(min_pos, max_pos + 1)
    ]
    return min(fuel_consumptions)


positions = get_input_positions()

print(f"fuel_consumption for best position: {best_fuel_consumption(positions, basic_crab_fuel_consumption)}")
print(f"fuel_consumption for crab best position: {best_fuel_consumption(positions, engineering_crab_fuel_consumption)}")
