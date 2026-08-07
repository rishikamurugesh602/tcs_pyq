H = int(input())
M = int(input())

if H > 24:
    print(f"-{H - 24}::{M}")
else:
    if M == 0:
        print(f"{24 - H}::0")
    else:
        print(f"{23 - H}::{60 - M}")
