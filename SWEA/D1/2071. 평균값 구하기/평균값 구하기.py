# 2071

T = int(input())

for t in range(1, T + 1) :
    numbers = list(map(int, input().split()))
    result = sum(numbers)
    result /= len(numbers)
    print(f'#{t} {round(result)}')