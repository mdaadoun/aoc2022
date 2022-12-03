sample = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

def get_priority(c):
    if c >= ord('a') and c <= ord('z'):
        return c - ord('a') + 1
    if c >= ord('A') and c <= ord('Z'):
        return c - ord('A') + 27

def part1(input):
    print("part 1:")
    total = []
    for i in input:
        done = False
        str1 = i[slice(0, int(len(i)/2))]
        str2 = i[slice(int(len(i)/2), len(i))]
        for a in str1:
            for b in str2:
                if a == b:
                    if not done:
                        total.append(get_priority(ord(a)))
                        done = True
    print(sum(total))

def part2(input):
    print("part 2:")
    total = []

    idx = 0
    while(idx < len(input)):
        done = False
        str1 = input[idx]
        str2 = input[idx + 1]
        str3 = input[idx + 2]
        for a in str1:
            for b in str2:
                for c in str3:
                    if a == b == c:
                        if not done:
                            total.append(get_priority(ord(a)))
                            done = True
        idx += 3
    print(sum(total))


if __name__ == '__main__':
    input = sample.split('\n')
    part1(input)
    part2(input)
    sample = open("output").read()
    input = sample.split('\n')
    part1(input)
    part2(input)
