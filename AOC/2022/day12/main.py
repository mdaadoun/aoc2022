# Use the Breadth First Search
# https://www.youtube.com/watch?v=oDqjPvD54Ss
# https://www.youtube.com/watch?v=KiCBXu4P-2Y

checks = {
    "down": (0, 1),
    "right": (1, 0),
    "left": (-1, 0),
    "top": (0, -1)
}

_map = {}
adjacency_list = {}

_start = ''
_exit = ''
_height = 0
_width = 0

visited = []


def reset_visited():
    global visited
    visited = []
    for y in range(_height):
        visited.append([])
        for x in range(_width):
            visited[y].append(False)


def reset():
    global _map, adjacency_list, _start, _exit, _height, _width
    _map = {}
    adjacency_list = {}

    _start = ''
    _exit = ''
    _height = len(input)
    _width = len(input[0])


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
                    if _map[tile] + 1 >= _map[adjacent_tile]:
                        adjacency_list[tile].append(adjacent_tile)


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


def get_coord(coord):
    x = int(coord.split(':')[0][1:])
    y = int(coord.split(':')[1][1:])
    return x, y


def solve(s):
    global visited
    start_coord = get_coord(s)
    row_queue = [start_coord[0]]
    column_queue = [start_coord[1]]
    visited[start_coord[1]][start_coord[0]] = True
    move_count = 0
    nodes_left_in_layer = 1
    nodes_in_next_layer = 0
    path = []
    while len(row_queue) or len(column_queue):
        x = row_queue.pop(0)
        y = column_queue.pop(0)
        coord = 'x' + str(x) + ":" + 'y' + str(y)
        if coord == _exit:
            path.append(coord)
            break
        for a in adjacency_list[coord]:
            a_coord = get_coord(a)
            if not visited[a_coord[1]][a_coord[0]]:
                visited[a_coord[1]][a_coord[0]] = True
                row_queue.append(a_coord[0])
                column_queue.append(a_coord[1])
                nodes_in_next_layer += 1
        nodes_left_in_layer -= 1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            path.append(coord)
            move_count += 1
    if _exit not in path:
        move_count = -1
    return move_count


def part1(input):
    print("part 1:")

    reset()
    reset_visited()
    build_map()
    build_adjacency_list()
    result = solve(_start)
    print(result)


def part2(input):
    global visited
    print("part 2:")

    reset()
    reset_visited()
    build_map()
    build_adjacency_list()
    all_starts = []
    results = []
    for m in _map:
        if _map[m] == 1:
            all_starts.append(m)
    for s in all_starts:
        reset_visited()
        r = solve(s)
        if r > 0:
            results.append(r)
    print(sorted(results)[0])


if __name__ == '__main__':
    sample = open("sample").read()
    input = sample.split('\n')
    part1(input)
    part2(input)
    sample = open("input").read()
    input = sample.split('\n')
    part1(input)
    part2(input)
