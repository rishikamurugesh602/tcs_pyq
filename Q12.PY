N = int(input())
R1 = int(input())
R2 = int(input())
R3 = int(input())

def solution(N, R1, R2, R3):
    count = 0

    # Buy plastic bottles
    count += N // R1
    N = N % R1

    # Buy glass bottles and exchange empty bottles
    while N >= R2:
        N -= R2
        count += 1
        N += R3

    return count

print(solution(N, R1, R2, R3))
