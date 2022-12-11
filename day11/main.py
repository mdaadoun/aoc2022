monkeys = {}
result = 0
modulo = 1


def reset():
    global monkeys, result
    monkeys = {}
    result = 0
    modulo = 1


def add_items(monkey, line):
    items = line.split(': ')[1:][0].split(', ')
    monkeys[monkey]['items'] = []
    for i in items:
        monkeys[monkey]['items'].append(int(i))


def parse(input):
    m = ''
    for line in input:
        l = line.split(' ')
        if l[0] == 'Monkey':
            m = 'm' + l[1][0]
            monkeys[m] = {"inspected_items": 0}
        if len(l) > 2:
            if l[2] == 'Starting':
                add_items(m, line)
            elif l[2] == 'Operation:':
                monkeys[m]["worry_increase"] = l[-2:]
                monkeys[m]["worry_decrease"] = 3
            else:
                if l[2] == 'Test:':
                    monkeys[m]['is_divisible_by'] = int(l[-1])
                if l[5] == 'true:':
                    monkeys[m]["true_next_monkey"] = 'm' + l[-1]
                if l[5] == 'false:':
                    monkeys[m]["false_next_monkey"] = 'm' + l[-1]


def send_items_to_next_monkeys(monkey):
    next_monkey = ''
    for item in monkeys[monkey]["items"]:
        if item % monkeys[monkey]['is_divisible_by'] == 0:
            next_monkey = monkeys[monkey]["true_next_monkey"]
        else:
            next_monkey = monkeys[monkey]["false_next_monkey"]
        monkeys[next_monkey]["items"].append(item)
    monkeys[monkey]["items"] = []


def monkeys_round(turn, part):
    for t in range(turn):
        for m in range(len(monkeys)):
            monkey = "m" + str(m)
            for idx, item in enumerate(monkeys[monkey]['items']):
                monkeys[monkey]["inspected_items"] += 1
                increase = monkeys[monkey]["worry_increase"]
                value = increase[1]
                if value == 'old':
                    value = int(item)
                else:
                    value = int(value)
                if increase[0] == '+':
                    monkeys[monkey]['items'][idx] += value
                else:
                    monkeys[monkey]['items'][idx] *= value
                if part == 1:
                    monkeys[monkey]['items'][idx] //= monkeys[monkey]["worry_decrease"]
                else:
                    monkeys[monkey]['items'][idx] %= modulo
            send_items_to_next_monkeys(monkey)


def solve():
    global result
    inspections = []
    for m in monkeys.keys():
        inspections.append(monkeys[m]["inspected_items"])
    inspections = sorted(inspections)
    result = inspections[-1] * inspections[-2]


def part1(input):
    print("part 1:")

    reset()
    parse(input)
    monkeys_round(20, 1)
    solve()
    print(result)


def part2(input):
    global modulo
    print("part 2:")

    reset()
    parse(input)
    for m in monkeys.keys():
        modulo *= monkeys[m]["is_divisible_by"]
    monkeys_round(10000, 2)
    solve()
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
