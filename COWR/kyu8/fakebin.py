
def fake_bin(str):
    fake = ''
    for c in str:
        if int(c) < 5:
            fake += '0'
        else:
            fake += '1'
    return fake

    # or
    # return ''.join('0' if c < '5' else '1' for c in str)


print(fake_bin('12342376849837'))