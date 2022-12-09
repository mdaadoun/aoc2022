HEAD = "head"
BODY = "body"
TAIL = "tail"
START = "x0y0"
size = 0
tiles = {
    "unknown": '.',
    "tail": 'T',
    "head": 'H',
    "visited": '#'
}
world = {}
rope = {}
visited = []


def reset(s=0):
    global world, rope, visited, size
    visited = [START]
    world = {
        "end_x": 0,
        "end_y": 0,
        "start_x": 0,
        "start_y": 0,
        START: tiles[HEAD]
    }
    rope = {
        HEAD: {'x': 0, 'y': 0, 'prev_x': 0, 'prev_y': 0},
        BODY: [START],
        TAIL: {'x': 0, 'y': 0}
    }
    size = s


def update_world():
    x = rope[HEAD]["x"]
    y = rope[HEAD]["y"]
    if x < world["start_x"]:
        world["start_x"] -= 1
    elif x > world["end_x"]:
        world["end_x"] += 1
    elif y < world["start_y"]:
        world["start_y"] -= 1
    elif y > world["end_y"]:
        world["end_y"] += 1
    world['x' + str(x) + 'y' + str(y)] = tiles[HEAD]
    world['x' + str(rope[TAIL]["x"]) + 'y' + str(rope[TAIL]["y"])] = tiles[TAIL]


def update_body(check):
    if len(rope[BODY]) < size - 1:
        if check in rope[BODY]:
            rope[BODY].append(check)
    else:
        if check != rope[BODY][-1]:
            rope[BODY].pop(0)
            rope[BODY].append(check)
    display_body()

    print(rope[BODY])

def update_tail():
    hx = rope[HEAD]['x']
    hy = rope[HEAD]['y']
    tx = rope[TAIL]['x']
    ty = rope[TAIL]['y']
    if tx + 2 == hx and ty == hy:
        rope[TAIL]['x'] += 1
    elif tx - 2 == hx and ty == hy:
        rope[TAIL]['x'] -= 1
    elif ty + 2 == hy and tx == hx:
        rope[TAIL]['y'] += 1
    elif ty - 2 == hy and tx == hx:
        rope[TAIL]['y'] -= 1

    elif (tx + 1 == hx and ty - 2 == hy) or (tx + 2 == hx and ty - 1 == hy):
        rope[TAIL]['x'] += 1
        rope[TAIL]['y'] -= 1
    elif (tx + 1 == hx and ty + 2 == hy) or (tx + 2 == hx and ty + 1 == hy):
        rope[TAIL]['x'] += 1
        rope[TAIL]['y'] += 1
    elif (tx - 1 == hx and ty - 2 == hy) or (tx - 2 == hx and ty - 1 == hy):
        rope[TAIL]['x'] -= 1
        rope[TAIL]['y'] -= 1
    elif (tx - 1 == hx and ty + 2 == hy) or (tx - 2 == hx and ty + 1 == hy):
        rope[TAIL]['x'] -= 1
        rope[TAIL]['y'] += 1

    check = 'x' + str(rope[TAIL]['x']) + 'y' + str(rope[TAIL]['y'])
    if size == 0:
        if check not in visited:
            visited.append(check)
    else:
        update_body(check)

def move_rope(input):
    direction = input[0]
    nb_moves = int(input[1])

    for move in range(nb_moves):
        rope[HEAD]["prev_x"] = rope[HEAD]["x"]
        rope[HEAD]["prev_y"] = rope[HEAD]["y"]
        if direction == 'L':
            rope[HEAD]["x"] -= 1
        elif direction == 'R':
            rope[HEAD]["x"] += 1
        elif direction == 'U':
            rope[HEAD]["y"] -= 1
        elif direction == 'D':
            rope[HEAD]["y"] += 1
        update_tail()
        update_world()


def display_visited():
    # print("World for position head at ", rope[HEAD], " and tail at ", rope[TAIL])
    for y in range(world['start_y'], world['end_y'] + 1):
        for x in range(world['start_x'], world['end_x'] + 1):
            tile = 'x' + str(x) + 'y' + str(y)
            if tile in visited:
                print(tiles['visited'], end='')
            else:
                print(tiles['unknown'], end='')
        print()


def display_body():
    print("body")
    for i in range(len(rope[BODY])):
        print(size - i, rope[BODY][i])

def part1(input):
    global world, rope
    print("part 1:")

    reset()
    for i in input:
        move_rope(i.split())
    display_visited()
    print(len(visited))


def part2(input):
    print("part 2:")

    reset(10)
    for i in input:
        move_rope(i.split())
    display_body()
    print(len(visited))


if __name__ == '__main__':
    sample = open("sample").read()
    input = sample.split('\n')
    # part1(input)
    part2(input)
    sample = open("sample2").read()
    input = sample.split('\n')
    # part1(input)
    # part2(input)
    sample = open("input").read()
    input = sample.split('\n')
    # part1(input)
    # part2(input)
