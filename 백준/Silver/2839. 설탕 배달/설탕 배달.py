N = int(input())

L = int(N // 5) # 나누어 떨어질 때 답이 되고 남으면 
result = -1
for l in range(L, -1, -1) : # l = large(5kg개수), s = small(3kg개수)
    s = 0

    while l*5 + s*3 < N :
        s += 1

    if l*5 + s*3 == N :
        result = l + s
        break

print(result)

    
