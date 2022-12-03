def get_common_item(s):
    s.strip()
    a, b = s[:len(s)//2], s[len(s)//2:]

    return set(a).intersection(set(b)).pop()


def get_priority(c):
    if ord(c) > ord('a'):
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 1 + 26


def solve_challenge_star1(input):
    summary = 0
    for line in input:
        c = get_common_item(line)
        summary += get_priority(c)
    print(summary)


def get_common_list_item(l1, l2, l3):
    return set(l1.strip()).intersection(set(l2.strip())).intersection(set(l3.strip())).pop()


def solve_challenge(input):
    summary = 0
    for idx in range(0, len(input), 3):
        c = get_common_list_item(input[idx], input[idx+1], input[idx+2])
        summary += get_priority(c)

    print(summary)


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        INPUT = f.readlines()
    solve_challenge(INPUT)

