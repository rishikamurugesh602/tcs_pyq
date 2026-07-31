n=int(input())
values=list(map(int,input().split()))
end=int(input())
def solve(index,arr,values,n):
    if index==n-1:
        if arr[index]!=arr[index-1]:
            return 1
        return 0
    count=0
    for val in values:
        if val!=arr[index-1]:
            arr[index]=val
            count+=solve(index+1,arr,values,n)
    return count

def countArrangements(n, values, end):
    arr = [0] * n
    arr[0] = 1
    arr[n - 1] = end

    return solve(1, arr, values, n)
print(countArrangements(n,values,end))
