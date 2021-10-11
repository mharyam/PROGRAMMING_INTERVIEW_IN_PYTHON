# define your sum_to_one() function above the function call

def sum_to_one(n):
    # print(n)
    if n == 0:
        return 0
    total = n + sum_to_one(n-1)
    return total


print(sum_to_one(4))