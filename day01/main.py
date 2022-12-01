sample = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def main(input):
    idx = 0
    tmp = []
    arr = []
    for i in input:
        if i != '':
            tmp.append(i)
        if i == '':
            arr.append(sum(tmp))
            tmp = []
    print(arr)
    print("Result part1:")
    print(max(arr))
    print("Result part2:")
    arr = sorted(arr)
    print(arr[-1] + arr[-2] + arr[-3])

if __name__ == '__main__':
    input = sample.split('\n')
    for i in range(len(input)):
        if input[i] != '':
            input[i] = int(input[i])
    main(input)
    sample = open("output").read()
    input = sample.split('\n')
    for i in range(len(input)):
        if input[i] != '':
            input[i] = int(input[i])
    main(input)
