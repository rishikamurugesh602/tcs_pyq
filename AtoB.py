n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def solution():
    pos = {}

    for i in range(n):
        pos[B[i]] = i

    perm = []

    for x in A:
        perm.append(pos[x])

    visited = [False] * n
    swaps = 0

    for i in range(n):

        if visited[i] or perm[i] == i:
            continue

        j = i
        cycle_size = 0

        while not visited[j]:
            visited[j] = True
            j = perm[j]
            cycle_size += 1

        swaps += cycle_size - 1

    return swaps

print(solution())
