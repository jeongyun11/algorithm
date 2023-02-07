import sys
N = int(sys.stdin.readline())
list1 = [int(sys.stdin.readline()) for n in range(N)]
# print(list1)
max_num = 0
cnt = 0
for n in list1[::-1] :
    if n > max_num :
        max_num = n
        cnt += 1

print(cnt)