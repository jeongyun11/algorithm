import sys
input = sys.stdin.readline
X, Y = map(int, input().split())
matrix = [list(map(int, input().split())) for x in range(X)]
# print(matrix)



for k in range(int(input())) :
    i, j, x, y = map(int, input().split())

    result = 0
    for x2 in range(i-1, x) :
        result += sum(matrix[x2][j-1:y])

        
            
            #if x-1 == x2 and y-1 == y2 :
    print(result)