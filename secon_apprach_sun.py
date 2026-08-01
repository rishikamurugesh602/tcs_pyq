day = input().lower()
n = int(input())

days = {
    "mon": 6,
    "tue": 5,
    "wed": 4,
    "thu": 3,
    "fri": 2,
    "sat": 1,
    "sun": 0
}

offset = days[day[:3]]

if n >= offset:
    ans = 1 + (n - offset) // 7
else:
    ans = 0

print(ans)
