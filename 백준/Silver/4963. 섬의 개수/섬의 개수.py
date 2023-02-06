import sys
while True :
    X, Y = map(int, sys.stdin.readline().strip().split())
    if X == 0 or Y == 0 :
        break
    matrix1 = [list(map(int, sys.stdin.readline().strip().split())) for y in range(Y)]
    # print(matrix1)

    list_land = []
    dict_land = {}
    for y in range(Y) :
        for x in range(X) :
            if matrix1[y][x] == 1 :
                list_land.append((x,y))
                dict_land[(x,y)] = []
    # print(list_land)
    # print(dict_land)

    for i in range(len(list_land)) :
        for j in range(len(list_land)) :
            if list_land[i] != list_land[j] :
                if (list_land[i][0] - list_land[j][0]) in [-1, 0, 1] and (list_land[i][1] - list_land[j][1]) in [-1, 0, 1] :
                    dict_land[list_land[i]].append(list_land[j])
    # print(dict_land)

    visited = [False] * len(list_land)
    # print(visited)

    cnt = 0
    while False in visited :
        i = visited.index(False)
        stack = [list_land[i]]
        visited[i] = True

        while stack :
            # print(stack)
            for land in dict_land[stack.pop()] :
                list_land.index(land)
                if visited[list_land.index(land)] == False :
                    stack.append(land)
                    visited[list_land.index(land)] = True
        cnt += 1
    
    print(cnt)