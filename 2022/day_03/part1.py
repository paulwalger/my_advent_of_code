import string

priority_by_letter = {
    letter: priority for priority, letter in enumerate(string.ascii_letters, 1)
}


def main():
    with open("input.txt", "r") as input_file:
        rucksacks = [line.strip() for line in input_file]
        common_item_types = [
            (
                set(rucksack[: len(rucksack) // 2])
                & set(rucksack[len(rucksack) // 2 :])
            ).pop()
            for rucksack in rucksacks
        ]
        scores = [
            priority_by_letter[common_item_type]
            for common_item_type in common_item_types
        ]
        print(sum(scores))


if __name__ == "__main__":
    main()
