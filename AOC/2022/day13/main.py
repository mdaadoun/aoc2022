import json

pairs = {}
ordered = []

def reset():
    global pairs, ordered

    ordered = []
    pairs = {}


def parse(input):
    global pairs
    pair = 1
    pairs[str(pair)] = {}
    for i, packet in enumerate(input):
        if i % 3 == 0:
            pairs[str(pair)]["1"] = json.loads(packet)
        elif i % 3 == 1:
            pairs[str(pair)]["2"] = json.loads(packet)
        else:
            pair += 1
            pairs[str(pair)] = {}


def pair_in_order(pair):
    order = 'none'
    l1 = len(pair['1'])
    l2 = len(pair['2'])
    length = l1
    if l2 > l1:
        length = l2
    for i in range(length):
        try:
            left = pair['1'][i]
        except (KeyError, IndexError):
            return 'true'
        try:
            right = pair['2'][i]
        except (KeyError, IndexError):
            return 'false'
        if type(left) != type(right):
            if isinstance(left, int):
                left = [left]
            if isinstance(right, int):
                right = [right]
        if not isinstance(left, int):
            test = {'1': left, '2': right}
            order = pair_in_order(test)
            if order != 'none':
                return order
        else:
            if left < right:
                return 'true'
            elif left > right:
                return 'false'
    return order


def part1(input):
    print("part 1:")

    reset()
    result = 0
    parse(input)
    for indice in range(1, len(pairs) + 1):
        test = pair_in_order(pairs[str(indice)])
        if test == "true":
            result += indice
    print(result)

def is_ordered():
    for i in range(0, len(ordered) - 1):
        a = ordered[i]
        b = ordered[i + 1]
        pair = {'1': a, '2': b}
        if pair_in_order(pair) == 'false':
            return False
    return True

def part2(input):
    global ordered
    print("part 2:")

    reset()
    parse(input)
    idx = len(pairs) + 1
    pairs[str(idx)] = {'1': [[2]], '2': [[6]]}
    for i in range(1, len(pairs) + 1):
        ordered.append(pairs[str(i)]['1'])
        ordered.append(pairs[str(i)]['2'])
    while not is_ordered():
        for i in range(0, len(ordered) - 1):
            a = ordered[i]
            b = ordered[i + 1]
            pair = {'1': a, '2': b}
            if pair_in_order(pair) == 'false':
                ordered[i], ordered[i + 1] = ordered[i + 1], ordered[i]
    result = 1
    for i, o in enumerate(ordered):
        if o == [[6]] or o == [[2]]:
            result *= i + 1
    print(result)

if __name__ == '__main__':
    sample = open("sample").read()
    input = sample.split('\n')
    part1(input)
    part2(input)
    sample = open("input").read()
    input = sample.split('\n')
    part1(input)
    part2(input)
