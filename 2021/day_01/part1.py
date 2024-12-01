"""
Count the number of times a depth measurement
increases from the previous measurement.
"""

with open("input.txt", "r") as input_file:
    measurements = [int(m.rstrip()) for m in input_file]
    count = sum([1 if a > b else 0 for a, b in zip(measurements[1:], measurements[:-1])])
    print(count)
