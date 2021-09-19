def parity_check(x):
    result = 0
    while x:
        result ^= x & 1
        print(result)
        x >>= 1
    return result


print(parity_check(100000))