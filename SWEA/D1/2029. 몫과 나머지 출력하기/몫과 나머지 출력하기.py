# 2029

T = int(input())
for t in range(1, T + 1) :
    a, b = map(int, input().split())
    A = a // b # 몫 계산
    B = a % b # 나머지 계산

    print(f'#{t} {A} {B}')