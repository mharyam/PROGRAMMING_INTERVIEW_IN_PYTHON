
def multiply(A, B):
    sum_index = 1
    sum_multiply = 0
    for b in B[::-1]:
        sum_multiply += a_integer(A, b) * sum_index
        sum_index *= 10
    return sum_multiply


def a_integer(l, a):
    sum_index = 1
    sum_m = 0
    for i in l[::-1]:
        sum_m += a * i * sum_index
        sum_index *= 10
    return sum_m


def better_solution(num1, num2):
    sign = -1 if (num1[0] < 0) or(num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):

            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i+j+1] %= 10

    return [sign * result[0]] + result[1:]


print(multiply([1, 2, 3], [9, 8, 7]))
print(multiply([1, 0, 1, 2, 3, 4, 6, 5, 2, 3, 4, 8, 7, 8, 9, 9, 8], [6, 5, 7, 4, 6, 3, 1, 1, 5, 4, 5, 6, 4, 6, 4, 3, 1]))
print(better_solution([1, 2, 3], [9, 8, 7]))

print(multiply([1, 2], [7, 8]))
print(multiply([1, 2], [7, 8]))