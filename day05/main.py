sample = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

stacks = []

# set crates array and return stacks number
def setcrates(input):
    global stacks
    crates = []
    stacks = []
    for i in input:
        arr = []
        if (len(i) == 0):
            break
        for c, j in enumerate(i):
            if (c % 2):
                arr.append(j)
        crates.append(arr)

    nb_stacks = 0
    for i in crates[-1]:
        if i != ' ':
            nb_stacks += 1
            stacks.append([])
    crates.pop()
    crates = crates[::-1]

    x = 0
    for i in range(nb_stacks):
        for j in range(len(crates)):
            try:
                stacks[i].append(crates[j][x])
            except IndexError:
                stacks[i].append(' ')
        x += 2

def printstacks():
    for c in stacks:
        if len(c) != 0:
            print(c)


def cleanstacks():
    for i, v in enumerate(stacks):
        for x in range(len(v), 0, -1):
            if stacks[i][x - 1] == ' ':
                stacks[i].pop()

def solvestacks1(input):
    for i in input:
        t = i.split(' ')
        if t[0] == 'move':
            nb = int(t[1])
            fr = int(t[3]) - 1
            to = int(t[5]) - 1
            for r in range(0, nb):
                l = stacks[fr].pop()
                stacks[to].append(l)

def solvestacks2(input):
    for i in input:
        t = i.split(' ')
        if t[0] == 'move':
            nb = int(t[1])
            fr = int(t[3]) - 1
            to = int(t[5]) - 1
            tmp = []
            for r in range(0, nb):
                tmp.append(stacks[fr].pop())
            for r in range(0, nb):
                stacks[to].append(tmp.pop())

def part1(input):
    print("part 1:")
    setcrates(input)
    cleanstacks()
    solvestacks1(input)

    for i in range(0, len(stacks)):
        print(stacks[i].pop(), end="")
    print()


def part2(input):
    print("part 2:")
    setcrates(input)
    cleanstacks()
    solvestacks2(input)

    for i in range(0, len(stacks)):
        print(stacks[i].pop(), end="")
    print()


if __name__ == '__main__':
    input = sample.split('\n')
    part1(input)
    part2(input)
    sample = open("output").read()
    input = sample.split('\n')
    part1(input)
    part2(input)
