def unique_elements(n, arr):
    seen = set()
    unique_arr = []
    for x in arr:
        if x not in seen:
            unique_arr.append(x)
            seen.add(x)
    return unique_arr
n = int(input())
arr = list(map(int, input().split()))
print(*unique_elements(n,arr))
