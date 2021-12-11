# criteria definitions
MOST = "most"
LEAST = "least"


# functions
def get_bit_criteria(lines, idx, criteria):
    count = sum(int(line[idx]) for line in lines)
    if count >= float(len(lines)) / 2:
        return "1" if criteria == MOST else "0"
    return "0" if criteria == MOST else "1"


def filter_lines_by_bit_criteria(lines, idx, criteria):
    bit_criteria = get_bit_criteria(lines, idx, criteria)
    return filter(lambda x: x[idx] == bit_criteria, lines)


def get_rating(lines, criteria):
    current_idx = 0
    while len(lines) > 1:
        lines = filter_lines_by_bit_criteria(lines, idx=current_idx, criteria=criteria)
        current_idx += 1
    return int(lines[0], 2)


# main
with open("input.txt", "r") as input_file:
    lines = [line.rstrip() for line in input_file]
    oxygen_rating = get_rating(lines, criteria=MOST)
    co2_rating = get_rating(lines, criteria=LEAST)
    print(oxygen_rating, co2_rating)
    print(oxygen_rating * co2_rating)
