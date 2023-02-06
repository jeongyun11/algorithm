def find_land(matrix, stack, dxdy) :
    while stack :
        y, x = stack.pop()
        for y1, x1 in dxdy : 
            y_move = y + y1
            x_move = x + x1
            if 0 <= x_move < len(matrix[0]) and 0 <= y_move < len(matrix): # 행렬의 범위를 안 벗어나고
                if matrix[y_move][x_move] == 1 :# 그 값이 1이면
                    stack.append((y + y1, x + x1)) # 추가한다.
        matrix[y][x] = 0

while True :
    X, Y = map(int,input().split())

    if X == Y == 0 :
        break

    matrix = [list(map(int,input().split())) for y in range(Y)]
    cnt = 0

    for y in range(Y) :
        while 1 in matrix[y] :
            stack = [(y, matrix[y].index(1))]
            find_land(matrix, stack, [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)])
            cnt +=1

    print(cnt)