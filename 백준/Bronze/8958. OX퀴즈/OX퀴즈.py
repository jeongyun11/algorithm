T = int(input())
for t in range(T) :
    cnt = 0
    result = 0
    OXs = input()
    for a in OXs :
        if a == 'O' :
            cnt += 1
            result += cnt
        else :
            cnt = 0
    print(result)