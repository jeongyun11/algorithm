import sys
# sys.stdin = open('test.txt', 'r')
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
result = []
for number in range(M, N +1) :

    if number == 1 :
        continue
    elif number == 2 :
        result.append(number)
        continue

    cnt = True
    for i in range(2,number) : # 1은 확정이여서 제외하고 센다.
        if number % i == 0 : # 나누어 떨어진다.
            cnt = False
    
    if cnt == True :
        result.append(number)

if result :
    print(sum(result))
    print(min(result))
else :
    print(-1)