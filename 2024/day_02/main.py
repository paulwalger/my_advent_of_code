# https://adventofcode.com/2024/day/2

import itertools
from typing import Literal

# parse input

with open("input.txt", "r") as input_file:
    reports = []
    for row in input_file:
        reports.append(list(map(int, row.strip().split(" "))))


# part 1


def is_report_safe(report: list[int]) -> Literal[0, 1]:
    is_asc = report[0] < report[1]
    for a, b in itertools.pairwise(report):
        if (a < b) != is_asc or not (1 <= abs(a - b) <= 3):
            return 0
    return 1


number_safe_reports = sum([is_report_safe(report) for report in reports])

print(f"The total number of safe reports is {number_safe_reports}")


# part 2


def is_report_safe_with_dumpener(report: list[int]) -> Literal[0, 1]:
    for levels in itertools.combinations(report, len(report) - 1):
        if is_report_safe(levels):
            return 1
    return 0


number_safe_reports_with_dumpener = sum([is_report_safe_with_dumpener(report) for report in reports])

print(f"The total number of safe reports with the problem dumpener is {number_safe_reports_with_dumpener}")
