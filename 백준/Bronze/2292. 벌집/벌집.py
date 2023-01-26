# import sys
# sys.stdin = open("test.txt","r")

a = int(input())

i = 1 # 중앙에서 거리
num_add = 6 # 벌집 증가 수
num = 1 # 벌집 수
while num < a:
  num += num_add
  num_add += 6
  i += 1

  # print('num_add =',num_add)
  # print('num_ist =',num_ist)

print(i)

