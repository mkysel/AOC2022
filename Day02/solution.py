# this code is AWFUL!
# I know...

def solve_challenge_basic(input):
    rock = "A"
    paper = "B"
    scissor = "C"

    response_rock = "X"
    response_paper = "Y"
    response_scissor = "Z"

    score = 0

    for line in input:
        match_score = 0
        opponent, myself = line.split(' ')
        opponent = opponent.strip()
        myself = myself.strip()

        if opponent == rock:
            if myself == response_rock:
                match_score += 3  # tie
                match_score += 1  # rock
            elif myself == response_paper:
                match_score += 6  # win
                match_score += 2  # paper
            elif myself == response_scissor:
                match_score += 0  # loss
                match_score += 3  # scissor
            else:
                assert False, myself
        elif opponent == paper:
            if myself == response_rock:
                match_score += 0  # loss
                match_score += 1  # rock
            elif myself == response_paper:
                match_score += 3  # tie
                match_score += 2  # paper
            elif myself == response_scissor:
                match_score += 6  # win
                match_score += 3  # scissor
            else:
                assert False, myself
        elif opponent == scissor:
            if myself == response_rock:
                match_score += 6  # win
                match_score += 1  # rock
            elif myself == response_paper:
                match_score += 0  # loss
                match_score += 2  # paper
            elif myself == response_scissor:
                match_score += 3  # tie
                match_score += 3  # scissor
            else:
                assert False, myself
        else:
            assert False, opponent
        score += match_score

    print(score)


def solve_challenge(input):
    rock = "A"
    paper = "B"
    scissor = "C"

    need_loss = "X"
    need_tie = "Y"
    need_win = "Z"

    score = 0

    for line in input:
        match_score = 0
        opponent, myself = line.split(' ')
        opponent = opponent.strip()
        myself = myself.strip()

        if opponent == rock:
            if myself == need_loss:
                match_score += 0  # loss
                match_score += 3  # scissors
            elif myself == need_tie:
                match_score += 3  # tie
                match_score += 1  # rock
            elif myself == need_win:
                match_score += 6  # win
                match_score += 2  # paper
            else:
                assert False, myself
        elif opponent == paper:
            if myself == need_loss:
                match_score += 0  # loss
                match_score += 1  # rock
            elif myself == need_tie:
                match_score += 3  # tie
                match_score += 2  # paper
            elif myself == need_win:
                match_score += 6  # win
                match_score += 3  # scissor
            else:
                assert False, myself
        elif opponent == scissor:
            if myself == need_loss:
                match_score += 0  # loss
                match_score += 2  # paper
            elif myself == need_tie:
                match_score += 3  # tie
                match_score += 3  # scissor
            elif myself == need_win:
                match_score += 6  # win
                match_score += 1  # rock
            else:
                assert False, myself
        else:
            assert False, opponent
        score += match_score

    print(score)

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        INPUT = f.readlines()
    solve_challenge(INPUT)
