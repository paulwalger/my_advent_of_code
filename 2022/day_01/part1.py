def main():
    with open("input.txt", "r") as input_file:
        elves = []
        current_elf = 0
        for calorie in input_file:
            if calorie.rstrip() == "":
                elves.append(current_elf)
                current_elf = 0
            else:
                current_elf += int(calorie.rstrip())

        print(max(elves))


if __name__ == "__main__":
    main()
