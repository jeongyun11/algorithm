# 2846.
N = int(input())
he = list(map(int, input().split()))
start = he[0]
result = []

for i in range(1, N) :
    if he[i-1] < he[i] : 
        end = he[i]

        if (i == N-1) or (he[i] >= he[i+1]) :
            result.append(end - start)    

    else : 
        start = he[i]
if result :
    print(max(result))
else :
    print(0)