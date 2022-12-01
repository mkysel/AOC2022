def solve_challenge(input):
    elven_calories = []
    current_elf = 0
    for line in input:
        if not line.strip():
            elven_calories.append(current_elf)
            current_elf = 0
        else:
            current_elf += int(line.strip())

    if current_elf:
        elven_calories.append(current_elf)

    elven_calories.sort()

    print(elven_calories[-1])
    print(elven_calories[-1]+elven_calories[-2]+elven_calories[-3])


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        INPUT = f.readlines()
    solve_challenge(INPUT)

