HEAD = "head"
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
moves = {
    "orth": {
        "D": (0, 1),
        "U": (0, -1),
        "R": (1, 0),
        "L": (-1, 0)
    },
    "diag": {
        "DR": (1, 1),
        "UR": (1, -1),
        "DL": (-1, 1),
        "UL": (-1, -1)
    }
}


def reset(s = 2):
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
        HEAD: {'x': 0, 'y': 0}
    }
    for i in range(1, s):
        rope["tail" + str(i)] = {'x': 0, 'y': 0}
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
    for i in range(1, size):
        tile = str(i)
        if size == 0:
            tile = tiles[TAIL]
        world['x' + str(rope["tail" + str(i)]["x"]) + 'y' + str(rope["tail" + str(i)]["y"])] = tile

def is_adjacent(t, h):
    return max(abs(t[0] - h[0]), abs(t[1] - h[1])) == 1

def is_equal(t, h):
    return t[0] == h[0] and t[1] == h[1]

def is_linear(t, h):
    return t[0] == h[0] or t[1] == h[1]

def update_tail(direction, first, second):
    hx = rope[first]['x']
    hy = rope[first]['y']
    tx = rope[second]['x']
    ty = rope[second]['y']

    if not is_equal((tx, ty), (hx, hy)) and not is_adjacent((tx, ty), (hx, hy)):
        if is_linear((tx, ty), (hx, hy)) and len(direction) == 1:
            m = moves["orth"][direction]
        elif is_linear((tx, ty), (hx, hy)):
                if tx == hx:
                    m = moves["orth"][direction[0]]
                    direction = direction[0]
                elif ty == hy:
                    m = moves["orth"][direction[1]]
                    direction = direction[1]
        else:
            if direction[0] in ['D', 'U']:
                if tx < hx:
                    m = moves["diag"][direction[0] + 'R']
                    direction = direction[0] + 'R'
                else:
                    m = moves["diag"][direction[0] + 'L']
                    direction = direction[0] + 'L'
            elif direction[0] in ['R', 'L']:
                d = direction[0]
                if ty < hy or (len(direction) > 1 and direction[1] == 'D'):
                    m = moves["diag"]['D' + direction[0]]
                    direction = 'D' + direction[0]
                else:
                    m = moves["diag"]['U' + d]
                    direction = 'U' + direction[0]
            else:
                m = (0, 0)
        rope[second]['x'] += m[0]
        rope[second]['y'] += m[1]

    if size <= 2:
        check = 'x' + str(rope[second]['x']) + 'y' + str(rope[second]['y'])
        if check not in visited:
            visited.append(check)
    else:
        last = "tail" + str(size - 1)
        if second == last:
            check = 'x' + str(rope[last]['x']) + 'y' + str(rope[last]['y'])
            if check not in visited:
                visited.append(check)
    return direction

def move_rope(input):
    nb_moves = int(input[1])

    for move in range(nb_moves):
        direction = input[0]
        m = moves["orth"][direction]
        rope[HEAD]['x'] += m[0]
        rope[HEAD]['y'] += m[1]
        first = HEAD
        for s in range(1, size):
            check = "tail" + str(s)
            direction = update_tail(direction, first, check)
            first = check
        update_world()


def display_visited():
    for y in range(world['start_y'], world['end_y'] + 1):
        for x in range(world['start_x'], world['end_x'] + 1):
            tile = 'x' + str(x) + 'y' + str(y)
            if tile in visited:
                print(tiles['visited'], end='')
            else:
                print(tiles['unknown'], end='')
        print()

def display_world():
    for y in range(world['start_y'], world['end_y'] + 2):
        for x in range(world['start_x'], world['end_x'] + 2):
            empty = True
            if rope[HEAD]['x'] == x and rope[HEAD]['y'] == y:
                empty = False
                print(tiles[HEAD], end='')
            else:
                for s in range(1, size):
                    if size <= 2:
                        tile = tiles[TAIL]
                    else:
                        tile = str(s)
                    if rope['tail' + str(s)]['x'] == x and rope['tail' + str(s)]['y'] == y:
                        empty = False
                        print(tile, end='')
                        break
            if empty:
                print('.', end='')
        print()

def part1(input):
    global world, rope
    print("part 1:")

    reset()
    for i in input:
        move_rope(i.split())
    display_visited()
    display_world()
    print(len(visited))


def part2(input):
    print("part 2:")

    reset(10)
    for i in input:
        move_rope(i.split())
    display_visited()
    display_world()
    print(len(visited))


if __name__ == '__main__':
    sample = open("sample").read()
    input = sample.split('\n')
    part1(input)
    part2(input)
    sample = open("sample2").read()
    input = sample.split('\n')
    part1(input)
    part2(input)
    sample = open("input").read()
    input = sample.split('\n')
    part1(input)
    part2(input)
