a = int(input())

len = 1


while a > len : #a <= len 이면 끝
    a = a - len  # 위에서 대각선으로
    len += 1 # 대각선 시작 위치를 의미
if len % 2 == 0 :
    print(f"{a}/{len+1 - a}") # 지그재그순서
else :
    print(f"{len+1 - a}/{a}") # 지그재그순서

