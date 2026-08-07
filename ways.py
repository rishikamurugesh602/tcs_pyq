N = int(input())
X = int(input())
I = int(input())

def solution():
    ways = [0] * (N + 1)
    ways[I] = 1

    for i in range(I + 1, N + 1):
        for j in range(1, X + 2):
            if i - j >= I:
                ways[i] += ways[i - j]

    return ways[N]

print(solution())
