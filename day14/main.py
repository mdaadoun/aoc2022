FALL = 500
limits = {}
paths = {}
cave = []

def reset():
    global paths, limits, cave
    paths = {}
    limits = {
        "min_x": FALL,
        "max_x": FALL,
        "min_y": 0,
        "max_y": 0
    }
    cave = []

def parse(input):
    global paths
    for i, path in enumerate(input):
        paths[i] = []
        for rock in path.split(' -> '):
            x = int(rock.split(',')[0])
            y = int(rock.split(',')[1])
            if x < limits['min_x']:
                limits['min_x'] = x
            if x > limits['max_x']:
                limits['max_x'] = x
            if y > limits['max_y']:
                limits['max_y'] = y
            paths[i].append((x, y))

def display_cave():
    print("<", limits['min_x'], "|", limits['max_x'], ">")
    for row in range(len(cave)):
        print(row, end=' ')
        for column in range(len(cave[0])):
            print(cave[row][column], end='')
        print()

def build_cave():
    global cave
    for y in range(limits['min_y'], limits['max_y'] + 1):
        cave.append([])
        for x in range(limits['min_x'], limits['max_x'] + 1):
            row = y - limits['min_y']
            if row == 0 and x == FALL:
                cave[row].append('+')
            else:
                cave[row].append('.')

    for i in range(len(paths)):
        print(paths[i])

def part1(input):
    print("part 1:")

    result = 0
    reset()
    parse(input)
    build_cave()
    display_cave()
    print(result)


def part2(input):
    print("part 2:")

    result = 0
    reset()
    parse(input)
    print(result)

if __name__ == '__main__':
    sample = open("sample").read()
    input = sample.split('\n')
    part1(input)
    # part2(input)
    sample = open("input").read()
    input = sample.split('\n')
    # part1(input)
    # part2(input)
