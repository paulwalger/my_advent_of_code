"""
Count the number of times a depth measurement
increases from the previous measurement.
"""

with open("input.txt", "r") as input_file:
    measurements = [int(m.rstrip()) for m in input_file]
    count = 0

    for idx in range(1, len(measurements)):
        if measurements[idx] > measurements[idx - 1]:
            count += 1

    print(count)
