with open("input.txt", "r") as input_file:
    # transform each line into a list of bit [1, 0, 1, ...]
    lines = [map(int, list(line.rstrip())) for line in input_file]

    # count the number of 1 per column
    nb_1_per_columns = list(map(sum, zip(*lines)))

    # total number of lines
    nb_lines = len(lines)

    # calculate gama and epsilon
    gama = int("".join(["1" if nb_1 > nb_lines / 2 else "0" for nb_1 in nb_1_per_columns]), 2)
    epsilon = int("".join(["0" if nb_1 > nb_lines / 2 else "1" for nb_1 in nb_1_per_columns]), 2)

    print(f"gama: {gama}")
    print(f"epsilon: {epsilon}")
    print(f"power consumption {gama * epsilon}")
