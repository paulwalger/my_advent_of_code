def is_pair_fully_contained(assignement_a, assignement_b):
    ab, ae = map(int, assignement_a.split("-"))
    bb, be = map(int, assignement_b.split("-"))

    return ab <= bb <= be <= ae or bb <= ab <= ae <= be


def main():
    with open("input.txt", "r") as input_file:
        assignement_pairs = [line.strip().split(",") for line in input_file]
        print(sum([is_pair_fully_contained(a, b) for a, b in assignement_pairs]))


if __name__ == "__main__":
    main()
