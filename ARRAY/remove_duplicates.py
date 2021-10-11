import time


def remove_duplicate(A):
    new_list = []
    for i in A:
        if i in new_list:
            pass
        else:
            new_list.append(i)
    return len(new_list)


def count_unique(A):
    if not A:
        return 0
    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1

    return write_index


def my_count_unique(A):
    if not A:
        return 0
    write_index = 1
    for i in range(len(A)-1):
        if A[i+1] != A[i]:
            write_index += 1

    return write_index

# t = time.time()
# print(remove_duplicate([2, 3, 5, 5, 7, 11, 11, 11, 77, 73]))
# end_t = time.time()
# # print(end_t, t)
# print(" %s seconds for count unique ---" % (end_t - t))

# s = time.time()
# print(count_unique([2, 3, 5, 5, 7, 11, 11, 11, 77, 73]))
# end_s = time.time()
# print(s, end_s)
# print(" %s seconds for count unique ---" % (end_s - s))
#


print(my_count_unique([2, 3, 5, 5, 7, 11, 11, 11, 77, 73, 100, 100]))