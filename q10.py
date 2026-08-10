N=int(input())
a=[]
for _ in range(N):
    a.append(int(input()))
def is_transaction_possible(a,N):
    change_30=0
    change_60=0
    change_120=0
    for i in range(N):
        if a[i]==30:
            change_30+=1
        elif a[i]==60:
            if change_30>=1:
                change_30-=1
            else:
                return 0
            change_60+=1
        elif a[i]==120:
            if change_30>=1 and change_60>=1:
                change_30-=1
                change_60-=1
            else:
                return 0
            change_120+=1
    return 1
if is_transaction_possible(a,N)==1:
    print( "Transaction successs")
else:
    print("no")
    
