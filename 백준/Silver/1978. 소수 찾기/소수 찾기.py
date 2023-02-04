N = int(input())
numbers = list(map(int, input().split()))

result = 0
for number in numbers :

    if number == 1 :
        continue
    elif number == 2 :
        result += 1
        continue

    cnt = True
    for i in range(2,number) : # 1은 확정이여서 제외하고 센다.
        if number % i == 0 : # 나누어 떨어진다.
            cnt = False
    
    if cnt == True :
        result += 1

print(result)
        