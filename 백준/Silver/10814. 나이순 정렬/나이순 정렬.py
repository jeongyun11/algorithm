import sys
input = sys.stdin.readline

N = int(input())

list1 = [tuple(input().split()) for i in range(N)]

for x, y in sorted(list1, key = lambda x : int(x[0])) :
    print(x, y)