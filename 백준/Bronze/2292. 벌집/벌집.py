a = int(input())

i = 1 # 중앙에서 거리
num_add = 6
num_start = 0 # i 번째 층의 집의 양
num_end = 1 # i 번째 층의 집의 양

while True:
  if num_start < a <= num_end :
    break
  num_start = num_end
  num_end += num_add
  num_add += 6
  i += 1

  # print('num_add =',num_add)
  # print('num_ist =',num_ist)

print(i)

