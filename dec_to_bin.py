n=int(input())
def solution():
    temp=n
    bits=0
    while temp>0:
        bits+=1
        temp//=2
    mask=(1<<bits)-1
    return (n^mask)
print(solution())
        
