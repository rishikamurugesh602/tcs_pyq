H=int(input())
M=int(input())
curr=H*60+M
if curr>24*60:
    exceeded=curr-24*60
    hour=exceeded//60
    minn=exceeded%60
    print(f"{hour}::{minn}")
else:
    time=24*60-curr
    hour=time//60
    minn=time%60
    print(f"{hour}::{minn}")

    
