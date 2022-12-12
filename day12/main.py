steps = 0
map = {}
journeys = []
checks = {
    "down": (0, 1),
    "right": (1, 0),
    "left": (-1, 0),
    "top": (0, -1)
}
tests = 1

def reset():
    global steps, map, tests, journey
    steps = 0
    map = {}
    journeys = []
    tests = 1

def solve():
    pass

def display_map():
    print(map)
    # for line in map:
    #     for tile in line:
    #         print(tile, end=',')
    #     print()


def get_next_tile(tile):
    value = map[tile]
    tx = int(tile.split(":")[0][1:])
    ty = int(tile.split(":")[1][1:])
    print(tx, ty, value)
    next_tile = ''
    for c in checks:
        cx = tx + checks[c][0]
        cy = ty + checks[c][1]
        if 0 <= cx < map["width"] and 0 <= cy <= map["height"]:
            next_tile = "x" + str(cx) + ":" + "y" + str(cy)
            if map[next_tile] <= value + 1:
                break
    return next_tile

def solve():
    global tests
    tile = map['start']
    exit_reached = False
    idx = 0
    while tests:
        journeys.append([tile])
        while not exit_reached:
            tile = get_next_tile(tile)
            journeys[idx].append(tile)
            if map[tile] == 'E':
                exit_reached = True
        idx += 1
        break

    print(journeys)

def build_map():
    for y, line in enumerate(input):
        for x, tile in enumerate(line):
            coord = 'x' + str(x) + ":" + 'y' + str(y)
            if tile not in ['S', 'E']:
                map[coord] = ord(tile) - ord('a') + 1
            else:
                map[coord] = tile
                if tile == 'S':
                    map['start'] = coord
                else:
                    map['exit'] = coord
    map['height'] = len(input)
    map['width'] = len(input[0])

def part1(input):
    print("part 1:")
    build_map()
    solve()
    display_map()

def part2(input):
    print("part 2:")


if __name__ == '__main__':
    sample = open("sample").read()
    input = sample.split('\n')
    part1(input)
    # part2(input)
    sample = open("input").read()
    input = sample.split('\n')
    # part1(input)
    # part2(input)
