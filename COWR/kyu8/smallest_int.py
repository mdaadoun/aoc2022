def find_smallest_int(arr):
    """
    input: arr, a list of integers
    output: smallest integer in arr
    """
    # arr.sort()
    # return arr[0]
    # or
    return sorted(arr)[0]
    # or
    # return min(arr)

print(find_smallest_int([2, 10, 1, 33]))