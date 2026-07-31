n = int(input())
arr = list(map(int, input().split()))

def solution():
    count_zero = 0
    count_neg = 0
    max_neg = float('-inf')
    product = 1

    for x in arr:
        if x == 0:
            count_zero += 1
            continue

        if x < 0:
            count_neg += 1
            max_neg = max(max_neg, x)

        product *= x

    if count_zero == n:
        return 0

    if count_neg == 1 and count_neg + count_zero == n:
        return 0

    if count_neg % 2 == 1:
        product //= max_neg

    return product

print(solution())
