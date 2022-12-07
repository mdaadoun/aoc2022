sample = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

path = "/"
folders = {}
most = 100000
disk_space = 70000000
needed_space = 30000000

def parse(i):
    global path

    i = i.split(' ')
    if len(i):
        if i[0] == "$" and i[1] == "cd":
            if i[2] != "..":
                if i[2] != '/':
                    if len(folders) == 1:
                        path += i[2]
                    else:
                        path += "/" + i[2]
                if path not in folders:
                    folders[path] = {"bytes": 0}
            else:
                path = path.split("/")
                path = path[:-1]
                path = "/".join(path)
        if i[0].isnumeric():
            folders[path]["bytes"] += int(i[0])


def count():
    for k1 in folders.keys():
        for k2 in folders.keys():
            if k1 != k2:
                k3 = ''
                if k1 != '/':
                    k3 += k1 + "/"
                else:
                    k3 = '/'
                if k2.startswith(k3):
                    folders[k1]["bytes"] += folders[k2]["bytes"]


def solve1():
    result = 0
    for key in folders.keys():
        test = folders[key]["bytes"]
        if test < most:
            result += test
    print(result)

def solve2():
    used_space = disk_space - folders['/']["bytes"]
    missing_space = needed_space - used_space
    print(used_space, missing_space)
    possible_dir = []
    for i in folders:
        if folders[i]["bytes"] >= missing_space:
            possible_dir.append(folders[i]["bytes"])
    result = sorted(possible_dir)[::-1].pop()
    print(result)

def part1(input):
    global folders, path
    print("part 1:")

    path = "/"
    folders = {}
    for i in input:
        parse(i)
    count()
    solve1()
    # print(folders)
    # print(len(folders))


def part2(input):
    global folders, path
    print("part 2:")

    path = "/"
    folders = {}
    for i in input:
        parse(i)
    count()
    solve2()
    # print(folders)


if __name__ == '__main__':
    input = sample.split('\n')
    # part1(input)
    part2(input)
    sample = open("output").read()
    input = sample.split('\n')
    # part1(input)
    part2(input)
