"""
Consider sums of a three-measurement sliding window.
How many sums are larger than the previous sum?
"""

with open("input.txt", "r") as input_file:
    measurements = [int(m.rstrip()) for m in input_file]
    count = 0

    for idx in range(0, len(measurements) - 3):
        sliding_window_1 = sum(measurements[idx : idx + 3])
        sliding_window_2 = sum(measurements[idx + 1 : idx + 4])

        if sliding_window_2 > sliding_window_1:
            count += 1
    print(count)
