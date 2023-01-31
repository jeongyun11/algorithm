# 1652.
Y = int(input())
X = Y
matrix = [list(input()) for y in range(Y)]
for y in range(Y) :
    matrix[y].append('X')
result1, result2 = 0, 0

for y in range(Y) :
    cnt = 0
    for x in range(X+1) :
        if matrix[y][x] == '.' :
            cnt +=1
            
        else :
            if cnt >= 2 :
                result1 += 1
            cnt = 0
        
matrix2 = [[[0] for x in range(X)] for y in range(Y)]
for y in range(Y) :
    for x in range(X) :
        matrix2[y][x] = matrix[x][y]

for y in range(Y) :
    matrix2[y].append('X')

for y in range(Y) :
    cnt = 0
    for x in range(X+1) :
        if matrix2[y][x] == '.' :
            cnt +=1
        else :
            if cnt >= 2 :
                result2 += 1
            cnt = 0
        

        
print(result1, result2)