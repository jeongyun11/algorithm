T = int(input())
for t in range(T) :
    X, Y = map(int, input().split())
    matrix = [list(map(int, input().split())) for y in range(X)]
    matrix_2 = [[0 for y in range(X)] for x in range(Y)]

    cnt = 0
    for x in range(X) :
        for y in range(Y) :
            matrix_2[y][x] = matrix[x][y]

    for y in range(Y) :
        for x in range(X) :
            if matrix_2[y][x] == 1 :
                cnt += matrix_2[y][x+1:].count(0)
    print(cnt)
