# https://adventofcode.com/2024/day/4


# parse input


with open("2024/day_05/input.txt", "r") as input_file:
    rows = [row.strip() for row in input_file.readlines()]
    rules = [list(map(int, row.split("|"))) for row in rows if "|" in row]
    page_orderings = [list(map(int, row.split(","))) for row in rows if "," in row]


# part 1


def is_pages_ordering_valid(pages, rules):
    for idx, page in enumerate(pages[:-1]):
        l_rules = [r[0] for r in rules if page == r[1]]
        if any([next_page in l_rules for next_page in pages[idx + 1 :]]):
            return False
    return True


sum_valid = sum([pages[len(pages) // 2] for pages in page_orderings if is_pages_ordering_valid(pages, rules)])

print(f"Sum of middle page orderings: {sum_valid}")

# part 2


def get_index_next_page_to_switch(
    pages: list[int],
    current_idx: int,
    rules: list[list[int, int]],
):
    for l_rule in [r[0] for r in rules if pages[current_idx] == r[1]]:
        for idx_next, next_page in enumerate(tmp_pages[current_idx + 1 :]):
            if next_page == l_rule:
                return current_idx + 1 + idx_next
    return 0


sum = 0

for pages in filter(lambda pages: not is_pages_ordering_valid(pages, rules), page_orderings):
    tmp_pages = pages.copy()
    idx = 0
    while idx < len(tmp_pages) - 1:
        next_page_to_switch = get_index_next_page_to_switch(tmp_pages, idx, rules)
        if next_page_to_switch:
            tmp_pages[idx], tmp_pages[next_page_to_switch] = tmp_pages[next_page_to_switch], tmp_pages[idx]
        else:
            idx += 1

    sum += tmp_pages[len(tmp_pages) // 2]

print(f"Sum of middle page orderings after fixing: {sum}")
