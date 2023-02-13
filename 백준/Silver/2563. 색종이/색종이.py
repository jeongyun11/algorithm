T = int(input())

matrix = [[0]*100 for y in range(100)]

for i in range(T) :
    Y, X = map(int, input().split())

    for y in range(Y, Y + 10) :
        for x in range(X, X + 10) :
            matrix[y][x] = 1

sum_mat = 0
for y in range(100) :
    sum_mat += sum(matrix[y])

print(sum_mat)