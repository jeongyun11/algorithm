matrix = [list(map(int,input().split())) for y in range(9)]
# pprint(matrix)
max_mat = 0

for y in range(9) :
    max_mat = max(max_mat, max(matrix[y]))

print(max_mat)

for y in range(9) :
    for x in range(9) :
        if matrix[y][x] == max_mat :
            print(y+1, x+1)
