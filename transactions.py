n = int(input())

transactions = []
fraud = set()
hashmap = {}

for i in range(n):
    sender, receiver, amount, timestamp = input().split()
    timestamp = int(timestamp)

    transactions.append((sender, receiver, amount, timestamp))

    key = (sender, receiver, amount)

    if key in hashmap:
        prev_index, prev_time = hashmap[key]

        if timestamp - prev_time <= 60:
            fraud.add(i)
            fraud.add(prev_index)

    hashmap[key] = (i, timestamp)

for i in range(n):
    if i not in fraud:
        print(*transactions[i])
