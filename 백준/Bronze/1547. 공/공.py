M = int(input())
cup_max = 0 # 컵 번호의 최댓값
change_list = []
result = 1
# 문제를 잘 읽자

for i in range(M) :
    cup_num = list(map(int,input().split()))

    for i in range(2) :
        if result == cup_num[i] :
            result = cup_num[1-i]
            break

print(result)