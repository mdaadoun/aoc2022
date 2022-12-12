# https://www.youtube.com/watch?v=oDqjPvD54Ss
# https://www.youtube.com/watch?v=KiCBXu4P-2Y

_map = {}
checks = {
    "down": (0, 1),
    "right": (1, 0),
    "left": (-1, 0),
    "top": (0, -1)
}
_start = ''
_exit = ''
adjacency_list = {}
_height = 0
_width = 0

def reset():
    global _map, adjacency_list, _start, _exit, _height, _width
    _map = {}
    _start = ''
    _exit = ''
    adjacency_list = []
    _height = 0
    _width = 0

def display_map():
    print(_map)

    print(_width, _height)
    for y in range(_height):
        for x in range(_width):
            tile = "x" + str(x) + ":" + "y" + str(y)
            print(_map[tile], end=', ')
        print()

    # for line in _map:
        # print(line)
        # for tile in line:
        #     print(tile, end=',')
        # for i in range(_width):
        # print(_map[line], end='')

        # print()


def build_adjacency_list():
    for y in range(_height):
        for x in range(_width):
            tile = "x" + str(x) + ":" + "y" + str(y)
            adjacency_list[tile] = []
            for c in checks:
                cx = x + checks[c][0]
                cy = y + checks[c][1]
                if 0 <= cx < _width and 0 <= cy < _height:
                    adjacent_tile = "x" + str(cx) + ":" + "y" + str(cy)
                    if adjacent_tile == _exit:
                        adjacency_list[tile].append(adjacent_tile)
                    elif _map[tile] + 1 >= _map[adjacent_tile]:
                        adjacency_list[tile].append(adjacent_tile)
    print(adjacency_list)

def build_map():
    global _start, _exit, _height, _width
    for y, line in enumerate(input):
        for x, tile in enumerate(line):
            coord = 'x' + str(x) + ":" + 'y' + str(y)
            if tile not in ['S', 'E']:
                _map[coord] = ord(tile) - ord('a') + 1
            else:
                if tile == 'S':
                    _start = coord
                    _map[coord] = ord('a') - ord('a') + 1
                else:
                    _exit = coord
                    _map[coord] = ord('z') - ord('a') + 1
    _height = len(input)
    _width = len(input[0])

def part1(input):
    print("part 1:")

    for i in input:
        print(i)
    build_map()
    build_adjacency_list()
    # display_adjacency_matrix()
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
