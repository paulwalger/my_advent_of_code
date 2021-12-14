def get_dots_input(file_name="dots_instructions_input.txt"):
    with open(file_name, "r") as dots_input_file:
        dots = {(int(x), int(y)) for x, y in [line.strip().split(",") for line in dots_input_file]}
        return dots


def get_folds_input(file_name="folds_instructions_input.txt"):
    with open(file_name, "r") as folds_input_file:
        folds = [
            (axis, int(value)) for axis, value in [line.strip().split(" ")[2].split("=") for line in folds_input_file]
        ]
        return folds


def is_y_axis(axis):
    return axis == "y"


def is_x_axis(axis):
    return axis == "x"


def symetric(x, y, axis, value):
    if is_y_axis(axis):
        if y > value:
            y = value - abs(y - value)
    elif is_x_axis(axis):
        if x > value:
            x = value - abs(x - value)
    return (x, y)


def get_dots_after_foldings(dots, folds):
    for fold_axis, fold_value in folds:
        new_dots = set()
        for dot in dots:
            new_dot = symetric(*dot, fold_axis, fold_value)
            new_dots.add(new_dot)
        dots = new_dots.copy()
    return dots


def display_origami_code(dots):
    width = max([dot[0] for dot in dots])
    height = max([dot[1] for dot in dots])
    code = []
    for y in range(height + 1):
        line = []
        for x in range(width + 1):
            if (x, y) in dots:
                line.append("#")
            else:
                line.append(".")
        code.append(line)

    for line in code:
        print(*line)


dots = get_dots_input()
folds = get_folds_input()

print(f"Number of remaining dots after first fold {len(get_dots_after_foldings(dots, folds[:1]))}")

print("Origami Code: ")
display_origami_code(get_dots_after_foldings(dots, folds))
