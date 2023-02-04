N = int(input())
result = []
i = 1
while True :

    if N == 1 :
        break
    
    i += 1

    if N % i == 0 :
        result.append(i)
        N = N/i
        i = 1


print(*result, sep='\n')