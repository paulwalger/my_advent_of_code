ROCK = "ROCK"
PAPER = "PAPER"
SCISSOR = "SCISSOR"

value_by_play = {
    ROCK: 1,
    PAPER: 2,
    SCISSOR: 3,
}

encrypted_to_play = {
    # opponent
    "A": ROCK,
    "B": PAPER,
    "C": SCISSOR,
}


def score_round(opponent_enc_play: str, expected_result: str):
    opponent_play = encrypted_to_play[opponent_enc_play]

    # draw
    if expected_result == "Y":
        return 3 + value_by_play[opponent_play]

    # victory
    if expected_result == "Z":
        return 6 + (value_by_play[opponent_play] % 3) + 1

    # lose
    my_score = value_by_play[opponent_play] - 1
    return 3 if my_score == 0 else my_score


def main():
    with open("input.txt", "r") as input_file:
        rounds = [line.strip().split() for line in input_file]
        scores = [score_round(round[0], round[1]) for round in rounds]
        print(sum(scores))


if __name__ == "__main__":
    main()
