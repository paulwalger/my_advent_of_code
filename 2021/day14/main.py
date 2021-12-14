import collections
import functools
import operator


def get_template(file_name="input.txt"):
    with open(file_name) as input_file:
        return list(input_file.readline().strip())


def get_pair_insertion(file_name="input.txt"):
    pair_insertion = {}
    with open(file_name) as input_file:
        for line in input_file.readlines()[2:]:
            pair, value = line.strip().split(" -> ")
            pair_insertion[pair] = value
    return pair_insertion


def sum_dicts(dicts):
    return dict(functools.reduce(operator.add, map(collections.Counter, dicts)))


def count_elements_recursively(pair, remaining_step, pair_insertion, memo={}):

    if (pair, remaining_step) in memo:
        return memo[(pair, remaining_step)]

    inserted_element = pair_insertion[pair]

    if remaining_step == 1:
        return {inserted_element: 1}

    counts = [{inserted_element: 1}]

    for new_pair in {pair[0] + inserted_element, inserted_element + pair[1]}:
        counts.append(count_elements_recursively(new_pair, remaining_step - 1, pair_insertion, memo))
    sum = sum_dicts(counts)
    memo[(pair, remaining_step)] = sum
    return sum


def get_count_by_elements_after_n_step(template, pair_insertion, nb_step):
    count_by_elements = {}
    memo = {}
    for elt in template:
        count_by_elements[elt] = count_by_elements.get(elt, 0) + 1
    counts = [count_by_elements]
    for i in range(len(template) - 1):
        pair = "".join(template[i : i + 2])
        counts.append(count_elements_recursively(pair, nb_step, pair_insertion, memo))
    return sum_dicts(counts)


def difference_between_most_and_least_occurences_after_steps(template, pair_insertion, nb_step):
    count_by_elements = get_count_by_elements_after_n_step(template, pair_insertion, nb_step)
    return max(count_by_elements.values()) - min(count_by_elements.values())


print(
    f"Difference after 10 steps: {difference_between_most_and_least_occurences_after_steps(get_template(), get_pair_insertion(), 10)}"
)
print(
    f"Difference after 40 steps: {difference_between_most_and_least_occurences_after_steps(get_template(), get_pair_insertion(), 40)}"
)
