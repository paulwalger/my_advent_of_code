def next_head_pos(current_pos, direction):
    if direction == "U":
        return (current_pos[0], current_pos[1] + 1)
    if direction == "D":
        return (current_pos[0], current_pos[1] - 1)
    if direction == "R":
        return (current_pos[0] + 1, current_pos[1])
    if direction == "L":
        return (current_pos[0] - 1, current_pos[1])


def next_tail_pos(current_pos, head_pos):
    """
    return the next position of the tail
    the tail move so it always touch the head (diagonnaly, overlapping counts)
    """

    delta_y = head_pos[1] - current_pos[1]
    delta_x = head_pos[0] - current_pos[0]
    dx, dy = 0, 0
    if abs(delta_y) == 2 and delta_x == 0:  # vertical
        dy = abs(delta_y) / delta_y
    elif abs(delta_x) == 2 and delta_y == 0:  # horizontal
        dx = abs(delta_x) / delta_x
    elif (abs(delta_x) + abs(delta_y)) > 2:  # not touching and not same row
        dx, dy = abs(delta_x) / delta_x, abs(delta_y) / delta_y
    return (current_pos[0] + dx, current_pos[1] + dy)


def nb_positions_tail(moves: list, nb_knots: int):
    tail_visited = {(0, 0)}
    knots = [(0, 0) for _ in range(nb_knots)]

    for move in moves:
        for _ in range(move[1]):
            # move head
            knots[0] = next_head_pos(knots[0], move[0])

            # move knots
            for knot_idx in range(1, nb_knots):
                knots[knot_idx] = next_tail_pos(knots[knot_idx], knots[knot_idx - 1])

            # add new tail pos
            tail_visited.add(knots[nb_knots - 1])

    return len(tail_visited)


def main():
    with open("input.txt", "r") as input_file:
        moves = list(
            map(
                lambda x: (x[0], int(x[1])),
                [line.strip().split() for line in input_file],
            )
        )

        print(nb_positions_tail(moves, 2))
        print(nb_positions_tail(moves, 10))


if __name__ == "__main__":
    main()
