sample = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

crates = []

# set crates array and return stacks number
def setcrates(input):
    global crates
    crates = [['']*20 for i in range(50)]
    lines = 0
    stacks = 0
    c = 25
    for i in input:
        for letter in i:
            if letter != '[' and letter != ']':
                crates[c].append(letter)
        if len(crates[c]) == 0:
            break
        c += 1
        lines += 1
    for i in crates[lines - 1]:
        if i != ' ':
            stacks += 1
    return stacks

def printcrates():
    for c in crates:
        if len(c) != 0:
            print(c)

def part1(input):
    print("part 1:")
    stacks = setcrates(input)
    print(crates)
    for i in input:
        cmd = i.split(' ')
        if cmd[0] == "move":
            nb_move = int(cmd[1])
            nb_from = int(cmd[3]) - 1
            nb_to   = int(cmd[5]) - 1
            for i in range(0, nb_move):
                for x in range(0, len(crates)):
                    if crates[x][nb_from * 2] != " ":
                        print(crates[x][nb_from * 2])
                        for y in range(len(crates), 0, -1):
                            print(y)
                            if crates[y][nb_to * 2] == " ":
                                print("move", crates[x][nb_from * 2], " from ", nb_from, " to ", nb_to)
                                crates[y][nb_to * 2] = crates[x][nb_from * 2]
                                crates[x][nb_from * 2] = " "
                                break
                        break
                printcrates()

    printcrates()


def part2(input):
    print("part 2:")


if __name__ == '__main__':
    input = sample.split('\n')
    part1(input)
    # part2(input)
    sample = open("output").read()
    input = sample.split('\n')
    # part1(input)
    # part2(input)
