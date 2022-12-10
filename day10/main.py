crt = {
    "width": 40,
    "height": 6,
    "screen": [],
    "pixel": {
        "off": ".",
        "on": "#"
    }
}
cpu = {}
check = [20, 60, 100, 140, 180, 220]
signal_strengths = []
sum_strengths = 0


def reset():
    global cpu, signal_strengths, sum_strengths, crt
    signal_strengths = []
    sum_strengths = 0
    cpu = {
        "nb_cycles": 0,
        "register": {
            "x": 1
        },
        "instructions": {
            "addx": {
                "cycles": 2,
                "value": 0
            },
            "noop": {
                "cycles": 1
            }
        }
    }
    crt["screen"] = []
    for x in range(crt["height"]):
        crt["screen"].append([])
        for y in range(crt["width"]):
            crt["screen"][x].append(crt["pixel"]["off"])


def draw_pixel():
    line = (cpu["nb_cycles"] - 1) // 40
    pixel = (cpu["nb_cycles"] - 1) % 40
    register = cpu["register"]["x"]

    if pixel in [register - 1, register, register + 1]:
        crt["screen"][line][pixel] = crt["pixel"]["on"]


def solve(input):
    global signal_strengths, sum_strengths
    for i in input:
        cmd = i.split()
        instruction = cmd[0]

        if instruction == "addx":
            cpu["instructions"][instruction]["value"] = int(cmd[1])
        instruction_cycles = cpu["instructions"][instruction]["cycles"]
        for ic in range(instruction_cycles):
            cpu["nb_cycles"] += 1
            draw_pixel()
            if cpu["nb_cycles"] in check:
                strength = cpu["nb_cycles"] * cpu["register"]["x"]
                signal_strengths.append(strength)
                sum_strengths += strength

        if instruction == "addx":
            cpu["register"]["x"] += cpu["instructions"][instruction]["value"]
            cpu["instructions"][instruction]["value"] = 0


def part1(input):
    print("part 1:")

    reset()
    solve(input)
    print(signal_strengths)
    print(sum_strengths)


def display_screen():
    for line in crt["screen"]:
        for pixel in line:
            print(pixel, end="")
        print()


def part2(input):
    print("part 2:")

    reset()
    solve(input)
    display_screen()


if __name__ == '__main__':
    sample = open("sample").read()
    input = sample.split('\n')
    part1(input)
    part2(input)
    sample = open("sample2").read()
    input = sample.split('\n')
    part1(input)
    part2(input)
    sample = open("input").read()
    input = sample.split('\n')
    part1(input)
    part2(input)
