def to_jaden_case(string):
    words = string.split()
    return ' '.join(word.capitalize() for word in words)


test = to_jaden_case("How can mirrors be real if our eyes aren't real")
print(test)