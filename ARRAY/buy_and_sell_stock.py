

def max_profit_check(A):
    max_profit = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
            if A[i] < A[j]:
                p = abs(A[i] - A[j])
                if p > max_profit:
                    # print(A[i], A[j])
                    max_profit = p

    return max_profit


def better_max_profit_check(A):
    max_profit = 0
    new_list = [0]
    for i in range(1, len(A)):
        if A[i-1] < A[i]:
            p = abs(A[i-1] - A[i])
        else:
            p = 0
        new_list.append(p)
        # if A[i-1] < A[i]:
        #     value

    print(new_list)
    return max(new_list)


print(max_profit_check([310, 315, 275, 295]))
print(max_profit_check([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
print(better_max_profit_check([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
