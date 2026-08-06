n, t = map(int, input().split())
pile = list(map(int, input().split()))

def nimsum(pile):
    xor = 0
    for stones in pile:
        xor ^= stones
    return xor

def solution():
    if nimsum(pile) != 0:
        if t == 1:
            return "Player 1 Wins"
        else:
            return "Player 2 Wins"
    else:
        if t == 1:
            return "Player 2 Wins"
        else:
            return "Player 1 Wins"

print(solution())
