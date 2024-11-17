n=int(input())
matrix=[list(map(int,input().split())) for _ in range(n)]
for row in matrix:
    row.reverse()
for row in matrix:
    print(*row)
