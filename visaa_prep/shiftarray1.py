def rotate_array(n, arr):
    return arr[1:] + arr[:1]
n = int(input())
arr = list(map(int, input().split()))
print(*rotate_array(n,arr))
