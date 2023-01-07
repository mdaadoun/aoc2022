grid = []
max_x = 0
max_y = 0
trees = {}  # coord x, y, height, bool visible


def build_grid(input):
    global max_x, max_y, grid

    max_x = 0
    max_y = 0
    grid = []
    for i, string in enumerate(input):
        grid.append([])
        for char in string:
            grid[i].append(char)

    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1


def build_forest():
    global trees

    trees = {}
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            trees["x:" + str(x) + " y:" + str(y)] = {
                "height": int(grid[y][x]),
                "visible": True,
                "view": 0
            }


def get_tree_data(x, y):
    tree = "x:" + str(x) + " y:" + str(y)
    height = trees[tree]['height']
    visible = trees[tree]['visible']
    view = trees[tree]['view']
    return height, visible, view


def set_tree_not_visible(x, y):
    tree = "x:" + str(x) + " y:" + str(y)
    trees[tree]['visible'] = False


def check_visibility(x, y):
    tree = get_tree_data(x, y)
    checks = {
        "top": (x, 0),
        "bottom": (x, max_y),
        "left": (0, y),
        "right": (max_x, y)
    }
    visible = False

    for k in checks.keys():
        cx = checks[k][0]
        cy = checks[k][1]
        while cx != x or cy != y:
            check = get_tree_data(cx, cy)
            if check[0] >= tree[0]:
                break
            if k == "top":
                cy += 1
            if k == "bottom":
                cy -= 1
            if k == "left":
                cx += 1
            if k == "right":
                cx -= 1
        if cx == x and cy == y:
            visible = True
            break

    if not visible:
        set_tree_not_visible(x, y)


def count_visible():
    count = 0

    for t in trees:
        if trees[t]["visible"]:
            count += 1
    return count


def solve1():
    last_tree_x = max_x
    last_tree_y = max_y

    cy = 1
    while cy < last_tree_y:
        cx = 1
        while cx < last_tree_x:
            check_visibility(cx, cy)
            cx += 1
        cy += 1


def check_scenic_view(x, y):
    tree = get_tree_data(x, y)
    views = {
        "top": 0,
        "bottom": 0,
        "left": 0,
        "right": 0
    }

    for v in views:
        cx = x
        cy = y
        while True:
            if v == "top":
                cy -= 1
            if v == "bottom":
                cy += 1
            if v == "left":
                cx -= 1
            if v == "right":
                cx += 1
            if cy < 0 or cy > max_y or cx < 0 or cx > max_x:
                break
            views[v] += 1
            check = get_tree_data(cx, cy)
            if tree[0] <= check[0]:
                break
    t = "x:" + str(x) + " y:" + str(y)
    r = views['top'] * views['bottom'] * views['left'] * views['right']
    trees[t]['view'] = r


def solve2():
    last_tree_x = max_x + 1
    last_tree_y = max_y + 1

    cy = 0
    while cy < last_tree_y:
        cx = 0
        while cx < last_tree_x:
            check_scenic_view(cx, cy)
            cx += 1
        cy += 1


def best_scenic_view():
    v = 0
    for t in trees:
        c = trees[t]['view']
        if c > v:
            v = c
    return v


def part1(input):
    print("part 1:")
    build_grid(input)
    build_forest()
    solve1()
    print(count_visible())


def part2(input):
    print("part 2:")
    build_grid(input)
    build_forest()
    solve2()
    print(best_scenic_view())


if __name__ == '__main__':
    sample = open("sample").read()
    input = sample.split('\n')
    part1(input)
    part2(input)
    sample = open("input").read()
    input = sample.split('\n')
    part1(input)
    part2(input)
