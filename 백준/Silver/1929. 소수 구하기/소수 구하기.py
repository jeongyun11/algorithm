import sys
# sys.stdin = open('test.txt', 'r')

# 1929.
M, N = map(int, sys.stdin.readline().split())
for i in range(M, N+1) :
    tnf = 1

    for j in range(2, int(i**0.5)+1) :
        if i % j == 0 :
            tnf = 0
            break

    if tnf == 1 and i != 1:
        print(i)

