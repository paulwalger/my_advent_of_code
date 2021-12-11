from itertools import permutations


SEGMENTS = "abcdefg"
PERMUTATIONS = permutations(SEGMENTS, 7)
NUMBERS = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg",
]


def get_input(file_name="input.txt"):
    with open(file_name, "r") as input_file:
        data = []
        for line in input_file:
            patterns, digits = line.strip().split(" | ")
            patterns = list(map(sorted, patterns.split(" ")))
            digits = digits.split(" ")
            data.append((patterns, digits))
        return data


class Permutation:
    def __init__(self, segments_permutation) -> None:
        self.segments_permutation = segments_permutation
        self.numbers = self.generate_numbers()

    def __str__(self) -> str:
        return str(self.segments_permutation)

    def generate_numbers(self):
        numbers = []
        for nb_segments in NUMBERS:
            numbers.append(
                sorted("".join([self.segments_permutation[SEGMENTS.index(segment)] for segment in nb_segments]))
            )
        return numbers

    def get_digits(self, coded_digits):
        digits = "".join([str(self.numbers.index(sorted(coded_digit))) for coded_digit in coded_digits])
        return int(digits)


def get_sum_digits(input):
    """Brut Force by testing all the permutations of abcdefg"""
    permu = [Permutation(permutation) for permutation in PERMUTATIONS]

    decoded_digits = []
    for patterns, digits in input:
        for permutation in permu:
            if all(pattern in permutation.numbers for pattern in patterns):
                decoded_digits.append(permutation.get_digits(digits))

    return sum(decoded_digits)


input = get_input("input.txt")
print(get_sum_digits(input))
