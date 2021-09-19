

def multiply(num1, num2):
    result = [0] * (len(num1) + len(num2))
    sign = -1 if num1[0] < 0 or num2[0] < 0 else 1
    # clean numbers
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])
    for i in reversed(range(len(num2))):
        for j in reversed(range(len(num1))):
            result[i + j + 1] += num2[i] * num1[j]
            result[i + j] += result[i + j + 1]//10
            result[i + j + 1] = result[i + j + 1] % 10

    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]


print(multiply([1, 2], [7, 8]))
