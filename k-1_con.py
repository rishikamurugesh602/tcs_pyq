N,K=map(int,input().split())
arr=list(map(int,input().split()))
def solution():
    l=0
    freq={}
    max_length=0
    for r in range(N):
        freq[arr[r]]=freq.get(arr[r],0)+1
        while len(freq)>K-1:
            freq[arr[left]]-=1
            if freq[arr[left]]==0:
                del freq[arr[left]]
            l+=1
        max_length=max(max_length,r-l+1)
    return max_length
        
            
print(solution())
