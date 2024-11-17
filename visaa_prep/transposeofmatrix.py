def transpose_matrix(n, matrix):
    return [[row[i] for row in matrix] for i in range(n)]
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
transposed = transpose_matrix(n, matrix)
for row in transposed:
    print(*row)
