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
    # me
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSOR,
}


def score_round(opponent_enc_play: str, my_enc_play: str):
    opponent_play = encrypted_to_play[opponent_enc_play]
    my_play = encrypted_to_play[my_enc_play]

    result_score = 0
    if opponent_play == my_play:
        result_score = 3
    if (
        opponent_play == ROCK
        and my_play == PAPER
        or opponent_play == PAPER
        and my_play == SCISSOR
        or opponent_play == SCISSOR
        and my_play == ROCK
    ):
        result_score = 6
    return value_by_play[my_play] + result_score


def main():

    with open("input.txt", "r") as input_file:
        rounds = [line.strip().split() for line in input_file]
        scores = [score_round(round[0], round[1]) for round in rounds]
        print(sum(scores))


if __name__ == "__main__":
    main()
