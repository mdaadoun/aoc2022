def find_needle(haystack):
    for idx in range(len(haystack)):
        if haystack[idx] == "needle":
            return "found the needle at position " + str(idx)
# or
# return 'found the needle at position %d' % haystack.index('needle')
# return 'found the needle at position {}'.format(haystack.index('needle'))

print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))
