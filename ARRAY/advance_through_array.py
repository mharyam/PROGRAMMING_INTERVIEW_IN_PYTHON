
def better_solution(A):
    count_mark = 0
    next_index = 0
    checker = 0

    while checker <= len(A) and next_index < len(A) - 1:
        max_counter = 0
        for index in range(next_index+1, A[next_index]+1):
            if A[index] > max_counter:
                print(index)
                max_counter = A[index]
                next_index = index
                count_mark += 1

        checker += 1
    return count_mark


def can_reach_end(l):
    furthest_reach_so_far, last_index = 0, len(l) - 1
    i = 0

    while i <= furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, l[i] + i)
        i += 1
    return furthest_reach_so_far >= last_index


# print(better_solution([3, 3, 7, 0, 2, 0, 1]))
# print(better_solution([3, 3, 1, 0, 2, 0, 1]))
print(can_reach_end([3, 3, 1, 0, 2, 0, 1]))
print(can_reach_end([3, 2, 0, 0, 2, 0, 7]))
# print(can_reach_end([2, 4, 1, 1, 0, 2, 3]))

