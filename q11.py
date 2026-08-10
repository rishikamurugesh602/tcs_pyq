string = input()

def solution():
    string_list = list(string)
    count = {}
    ans = 0

    for i in range(len(string_list)):
        count[string_list[i]] = count.get(string_list[i], 0) + 1

    string_list.sort()

    for i in range(1, len(string_list)):
        if count[string_list[i]] % 2 == 0:
            if string_list[i] == string_list[i-1]:
                ans += 1
    return ans

print(solution())
