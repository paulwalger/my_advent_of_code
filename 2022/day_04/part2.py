def is_pair_overlaping(assignement_a, assignement_b):
    ab, ae = map(int, assignement_a.split("-"))
    bb, be = map(int, assignement_b.split("-"))

    return ab <= bb <= ae or ab <= be <= ae or bb <= ab <= be or bb <= ae <= be


def main():
    with open("input.txt", "r") as input_file:
        assignement_pairs = [line.strip().split(",") for line in input_file]
        print(sum([is_pair_overlaping(a, b) for a, b in assignement_pairs]))


if __name__ == "__main__":
    main()
