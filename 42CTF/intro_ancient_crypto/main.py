def main(input):
    first = ord('A')
    last = ord('Z')
    rotmax = 16
    rot = 0

    while (rotmax):
        print(rotmax, ":")
        print("42CTF{", end="")
        for i in input:
            c = ord(i)
            if first <= c <= last:
                while rot < rotmax:
                    c += 1
                    if c > last:
                        c = first
                    rot += 1
            if i != '\n':
                print(chr(c), end="")
            rot = 0
        print("}")
        rotmax -= 1


if __name__ == '__main__':
    input = open("output").read()
    print(input)
    main(input)
