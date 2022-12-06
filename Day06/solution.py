def solve_challenge(input: str, message_length: int) -> int:
    # just one string in input
    signal = input[0]

    for idx in range(message_length, len(signal)):
        if len(set(signal[idx-message_length:idx])) == message_length:
            return idx


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        INPUT = f.readlines()
    print(solve_challenge(INPUT, 4))
    print(solve_challenge(INPUT, 14))

