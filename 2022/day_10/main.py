def get_cycles_v(instructions):
    """generator that execute instructions and yield the value of x at each cycle"""
    x = 1

    for instruction in instructions:

        if instruction == "noop":
            yield x

        elif instruction.startswith("addx"):
            v = int(instruction.split()[1])
            yield x
            yield x
            x += v


def main():
    with open("input.txt", "r") as input_file:
        instructions = list(line.strip() for line in input_file)

        cycles = list(get_cycles_v(instructions))

        # part 1
        print(sum(cycle * cycles[cycle - 1] for cycle in (20, 60, 100, 140, 180, 220)))

        # part2
        current_cycle = 0
        rows = [[] for _ in range(6)]
        for row in rows:
            for crt_idx, cycle in enumerate(range(current_cycle, current_cycle + 40)):
                x = cycles[cycle]
                if crt_idx in (x - 1, x, x + 1):
                    row.append("#")
                else:
                    row.append(".")
            current_cycle += 40

        for row in rows:
            print("".join(row))


if __name__ == "__main__":
    main()
