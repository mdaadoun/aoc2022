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
    # print(grid)
    # print(len(grid))
    # print(grid[0][0])
    # print(max_x, max_y)
    # print(len(grid) - 1, len(grid[0]) - 1)
    # print(grid[max_y-1][max_x])


def build_forest():
    global trees

    trees = {}
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            trees["x:" + str(x) + " y:" + str(y)] = {
                "height": int(grid[y][x]),
                "visible": True
            }

    # print(trees)


def get_tree_data(x, y):
    tree = "x:" + str(x) + " y:" + str(y)
    height = trees[tree]['height']
    visible = trees[tree]['visible']
    return height, visible


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

    # print(x, y, tree[0])
    for k in checks.keys():
        cx = checks[k][0]
        cy = checks[k][1]
        # print(k, "check")
        while cx != x or cy != y:
            check = get_tree_data(cx, cy)
            if check[0] >= tree[0]:
                # print("The check hide the tree")
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
            # print("the tree is visible")
            visible = True
            break

    if not visible:
        set_tree_not_visible(x, y)
    # print("top", get_tree_data(top_tree[0], top_tree[1]))
    # print("bottom", get_tree_data(bottom_tree[0], bottom_tree[1]))
    # print("left", get_tree_data(left_tree[0], left_tree[1]))
    # print("right", get_tree_data(right_tree[0], right_tree[1]))


def solve1():
    last_tree_x = max_x
    last_tree_y = max_y

    counter_y = 1
    while (counter_y < last_tree_y):
        counter_x = 1
        while (counter_x < last_tree_x):
            check_visibility(counter_x, counter_y)
            counter_x += 1
            # print()
        counter_y += 1

def count_visible():
    count = 0

    for t in trees:
        if trees[t]["visible"]:
            count += 1
    return count

def part1(input):
    print("part 1:")
    build_grid(input)
    build_forest()
    solve1()
    print(count_visible())

def part2(input):
    print("part 2:")


if __name__ == '__main__':
    sample = open("sample").read()
    input = sample.split('\n')
    part1(input)
    # part2(input)
    sample = open("input").read()
    input = sample.split('\n')
    part1(input)
    # part2(input)
