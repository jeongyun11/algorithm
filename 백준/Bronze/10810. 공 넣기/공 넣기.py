N, M = map(int, input().split())
basket = [0] * N

for i in range(M):
    i, j, k = map(int, input().split())
    for a in range(i - 1, j) :
        basket[a] = k

print(*basket)