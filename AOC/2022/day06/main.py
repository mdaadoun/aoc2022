sample1 = """mjqjpqmgbljsphdztnvjfqwrcgsmlb""" #7
sample2 = """bvwbjplbgvbhsrlpgdmjqwftvncz""" #5
sample3 = """nppdvjthqldpwncqszvftbrmjlhg""" #6
sample4 = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg""" #10
sample5 = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw""" #11


def part1(input):
    print("part 1:")

    arr = input[::-1]
    found = False
    test = []
    idx = 4
    for i in range(4):
        test.append(arr.pop())
    while not found:
        if len(set(test)) != 4:
            test = test[1:]
            test.append(arr.pop())
            idx += 1
        else:
            found = True
    print(idx)

def part2(input):
    print("part 2:")

    arr = input[::-1]
    found = False
    test = []
    idx = 14
    for i in range(14):
        test.append(arr.pop())
    while not found:
        if len(set(test)) != 14:
            test = test[1:]
            test.append(arr.pop())
            idx += 1
        else:
            found = True
    print(idx)


if __name__ == '__main__':
    input = [*sample1]
    part1(input)
    part2(input)
    input = [*sample2]
    part1(input)
    part2(input)
    input = [*sample3]
    part1(input)
    part2(input)
    input = [*sample4]
    part1(input)
    part2(input)
    input = [*sample5]
    part1(input)
    part2(input)
    sample = open("output").read()
    input = [*sample]
    part1(input)
    part2(input)
