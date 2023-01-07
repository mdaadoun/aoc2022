def square_digits(num):
    digits = [int(d)**2 for d in str(num)]
    result = ''.join(str(n) for n in digits)
    return int(result)


print(square_digits(9119))