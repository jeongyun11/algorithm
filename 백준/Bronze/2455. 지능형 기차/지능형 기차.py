# 2455.
max_num = 0
cur = 0

for i in range(4) :
    o, i = map(int,input().split())
    cur += i - o

    max_num = max(cur, max_num)

print(max_num)