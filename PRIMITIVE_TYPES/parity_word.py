def count_bits(x):
    num_bits = 0
    while x:
        print(x, "XX")
        num_bits += x & 1
        print(x >> 1)
        x >>= 1
    return num_bits


# print(count_bits(110000001))
print(count_bits(60))
