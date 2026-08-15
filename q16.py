n = int(input())
B = list(map(int, input().split()))
arr = list(range(1, n+1))
ans=0
ar=[]
while True:
    ans+=1
    ar=[None]*n
    for i in range(n):
        ar[i]=arr[B[i]-1]
    if ar==sorted(ar):
        break
    arr=ar
print(ans)
