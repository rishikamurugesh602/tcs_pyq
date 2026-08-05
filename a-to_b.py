n=int(input())
A=input()
B=input()
def solution(A,B):
    A=list(A)
    ans=0
    n=len(A)
    for i in range(n):
        if A[i]<B[i]:
            return -1
    for ch in range(ord('z'),ord('a')-1,-1):
        target=None
        for i in range(n):
            if ord(A[i])==ch and A[i]!=B[i]:
                if target is None or B[i]>target:
                    target=B[i]
        if target is None:
            continue
        ans+=1
        for i in range(n):
            if ord(A[i])==ch and B[i]==target:
                A[i]=target
    return ans
                
print(solution(A,B))A_to
