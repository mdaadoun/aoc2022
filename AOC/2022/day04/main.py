sample = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def part1(input):
    print("part 1:")
    count = 0

    for i in input:
        elf1 = (int(i.split(',')[0].split('-')[0]), int(i.split(',')[0].split('-')[1]))
        elf2 = (int(i.split(',')[1].split('-')[0]), int(i.split(',')[1].split('-')[1]))

        if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]):
            count += 1
        elif (elf2[0] <= elf1[0] and elf2[1] >= elf1[1]):
            count += 1
    print(count)


def part2(input):
    print("part 2:")
    count = 0

    for i in input:
        elf1 = (int(i.split(',')[0].split('-')[0]), int(i.split(',')[0].split('-')[1]))
        elf2 = (int(i.split(',')[1].split('-')[0]), int(i.split(',')[1].split('-')[1]))
        for x in range(elf1[0], elf1[1] + 1):
            if x >= elf2[0] and x <= elf2[1]:
                count += 1
                break
    print(count)


if __name__ == '__main__':
    input = sample.split('\n')
    part1(input)
    part2(input)
    sample = open("output").read()
    input = sample.split('\n')
    part1(input)
    part2(input)
