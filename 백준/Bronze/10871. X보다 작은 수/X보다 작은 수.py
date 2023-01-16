
# 10871
n, x = map(int,input().split())
numbers = map(int,input().split())

for number in numbers :
    if number < x :
        print(number, end=' ')