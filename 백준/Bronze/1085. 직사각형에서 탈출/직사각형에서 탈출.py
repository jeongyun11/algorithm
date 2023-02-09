# import sys
# sys.stdin = open('test.txt', 'r')

x, y, w, h = map(int, input().split())

x = w-x if x > w/2 else x
y = h-y if y > h/2 else y
print(min(x,y))