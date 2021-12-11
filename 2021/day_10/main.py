from queue import LifoQueue

PAIRS = {"{}", "[]", "()", "<>"}
CORRUPTION_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}
COMPLETION_SCORES = {")": 1, "]": 2, "}": 3, ">": 4}


def get_input(file_name):
    with open(file_name, "r") as input_file:
        lines = [line.strip() for line in input_file]
        return lines


def is_opening(c):
    return c in {"<", "{", "(", "["}


def are_matching(opening_c, closing_c):
    return f"""{opening_c}{closing_c}""" in PAIRS


def get_matching_c(c):
    for pair in PAIRS:
        if c in pair:
            return pair[0] if c != pair[0] else pair[1]


def get_line_corruption_score(line):
    q = LifoQueue()
    for c in line:
        if is_opening(c):
            q.put(c)
        else:
            last_c = q.get()
            if not are_matching(last_c, c):
                return CORRUPTION_SCORES[c]
    return 0


def get_line_completion_score(line):
    opened_c = []
    for c in line:
        if is_opening(c):
            opened_c.append(c)
        else:
            opened_c.pop()

    score = 0
    for c in reversed(opened_c):
        score *= 5
        score += COMPLETION_SCORES[get_matching_c(c)]

    return score


def get_corruption_score(lines):
    return sum(get_line_corruption_score(line) for line in lines)


def get_completion_score(lines):
    scores = [
        get_line_completion_score(line) for line in filter(lambda line: not get_line_corruption_score(line), lines)
    ]
    scores.sort()
    return scores[len(scores) // 2]


lines = get_input("input.txt")

print(f"Corruption score {get_corruption_score(lines)}")
print(f"Completion score {get_completion_score(lines)}")
