b, n = map(int, input().split())
arr = list(map(int, input().split()))

def solution(b, arr):
    arr.sort()   # Fight in the optimal order

    for z in arr:
        if b < z:
            return "NO"
        b -= (z % 2) + (z // 2)

    return "YES"

print(solution(b, arr))
