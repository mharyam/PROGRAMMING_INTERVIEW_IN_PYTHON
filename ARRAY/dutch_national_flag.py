
def dutch_flag(A, index):
    index_value = A[index]
    print(index_value, "VALUEEEEEEE")
    low, mid, high = 0, 0, len(A) - 1
    while mid <= high:
        if A[mid] < index_value:
            A[mid], A[low] = A[low], A[mid]
            mid += 1
            low += 1
        elif A[mid] == index_value:
            mid += 1
        else:
            A[mid], A[high] = A[high], A[mid]
            high -= 1
    return A


def dutch_flag_partition(p_index, A) :
    pivot = A[p_index]
    # First pass: group elernents smal-ler than pivot
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    # Second pass; group elements Targer than pivot
    larger = len(A)-1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[i], A[larger]
            larger -= 1
    return A


print(dutch_flag([0, 1, 2, 0, 2, 1, 1], 2))
print(dutch_flag_partition(2, [0, 1, 2, 0, 2, 1, 1]))
