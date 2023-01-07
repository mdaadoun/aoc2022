sample = """A Y
B X
C Z"""

elf = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

score_shape = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

score_game = {
    "win": 6,
    "draw": 3,
    "lose": 0
}

you = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

strategy = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}

def part2(input):
    print("part 2:")
    score = []

    for i in input:
        if elf[i[0]] == "rock":
            if strategy[i[2]] == "win":
                score.append(int(score_shape["paper"]) + int(score_game[strategy[i[2]]]))
            if strategy[i[2]] == "draw":
                score.append(int(score_shape["rock"]) + int(score_game[strategy[i[2]]]))
            if strategy[i[2]] == "lose":
                score.append(int(score_shape["scissors"]) + int(score_game[strategy[i[2]]]))
        if elf[i[0]] == "paper":
            if strategy[i[2]] == "win":
                score.append(int(score_shape["scissors"]) + int(score_game[strategy[i[2]]]))
            if strategy[i[2]] == "draw":
                score.append(int(score_shape["paper"]) + int(score_game[strategy[i[2]]]))
            if strategy[i[2]] == "lose":
                score.append(int(score_shape["rock"]) + int(score_game[strategy[i[2]]]))
        if elf[i[0]] == "scissors":
            if strategy[i[2]] == "win":
                score.append(int(score_shape["rock"]) + int(score_game[strategy[i[2]]]))
            if strategy[i[2]] == "draw":
                score.append(int(score_shape["scissors"]) + int(score_game[strategy[i[2]]]))
            if strategy[i[2]] == "lose":
                score.append(int(score_shape["paper"]) + int(score_game[strategy[i[2]]]))
    print(sum(score))


def part1(input):
    print("part 1:")
    score = []

    for i in input:
        if elf[i[0]] == you[i[2]]:
            score.append(int(score_shape[you[i[2]]]) + int(score_game["draw"]))
        if elf[i[0]] == "rock" and you[i[2]] == "paper":
            score.append(int(score_shape[you[i[2]]]) + int(score_game["win"]))
        if elf[i[0]] == "rock" and you[i[2]] == "scissors":
            score.append(int(score_shape[you[i[2]]]) + int(score_game["lose"]))
        if elf[i[0]] == "paper" and you[i[2]] == "scissors":
            score.append(int(score_shape[you[i[2]]]) + int(score_game["win"]))
        if elf[i[0]] == "paper" and you[i[2]] == "rock":
            score.append(int(score_shape[you[i[2]]]) + int(score_game["lose"]))
        if elf[i[0]] == "scissors" and you[i[2]] == "rock":
            score.append(int(score_shape[you[i[2]]]) + int(score_game["win"]))
        if elf[i[0]] == "scissors" and you[i[2]] == "paper":
            score.append(int(score_shape[you[i[2]]]) + int(score_game["lose"]))
    print(sum(score))


if __name__ == '__main__':
    input = sample.split('\n')
    part1(input)
    part2(input)
    sample = open("output").read()
    input = sample.split('\n')
    part1(input)
    part2(input)
