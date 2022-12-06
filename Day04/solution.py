import re


def are_pairs_containing(pair1: tuple[int, int], pair2: tuple[int, int]) -> bool:
    min1, max1 = pair1
    min2, max2 = pair2
    return (min1 <= min2 and max2 <= max1) or (min2 <= min1 and max1 <= max2)


def are_pairs_overlapping(pair1: tuple[int, int], pair2: tuple[int, int]) -> bool:
    min1, max1 = pair1
    min2, max2 = pair2
    return (min1 <= min2 <= max1) or (min2 <= min1 <= max2)


def solve_challenge_basic(filename: str) -> int:
    assignments = parse_input(filename)
    count = 0
    for pair in assignments:
        if are_pairs_containing(pair[0], pair[1]):
            count += 1
    return count


def solve_challenge(filename: str) -> int:
    assignments = parse_input(filename)
    count = 0
    for pair in assignments:
        if are_pairs_overlapping(pair[0], pair[1]):
            count += 1
    return count


def parse_input(lines: str) -> list[list[tuple[int, int]]]:
    assignments = []
    for line in lines:
        a, b, c, d = map(int, re.findall(r"\d+", line))
        assignments.append([(a, b), (c, d)])
    return assignments


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        INPUT = f.readlines()
    print(solve_challenge_basic(INPUT))
    print(solve_challenge(INPUT))

