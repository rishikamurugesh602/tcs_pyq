day=input()
n=int(input())
def solution():
    first=0
    
    m = {
        "mon": 6, "tue": 5, "wed": 4,
        "thu": 3, "fri": 2, "sat": 1,
        "sun": 0
    }
    first=m[day]
    count=0
    while first<=n:
        count+=1
        first+=7
    return count
print(solution())
