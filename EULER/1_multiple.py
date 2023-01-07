def multiple(test):
    sum = 0
    for n in range(test):
        if not n % 3 or not n % 5:
            sum += n
    return sum

if __name__ == '__main__':
    print(multiple(1000))