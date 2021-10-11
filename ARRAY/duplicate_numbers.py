def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    expected_sum = sum(arr)
    current_sum = 0
    for i in range(len(arr) - 1):
        current_sum += i
    return current_sum - expected_sum


print(duplicate_number([0, 2, 3, 1, 4, 5, 3]))
