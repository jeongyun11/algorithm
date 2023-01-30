T = int(input())

for _ in range(T) :
    K = int(input())
    N = int(input())

    floor = [i for i in range(1, N + 1)]

    for k in range(K) :
        for n in range(N - 1,-1, -1) :
            floor[n] = sum(floor[:n+1])

    print(floor[-1])