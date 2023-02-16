# 10250
T = int(input())
for t in range(T) :
    h,w,n = map(int,input().split())
# 주소의 형태는 나머지 + 몫의 올림
    if n % h == 0 : # 나누어 떨어지면 
        if (n // h) < 10 : 
            print(str(h) + '0' + str(n // h) )
        else :
            print(str(h) + str(n // h) )
    else :
        if (n // h + 1) < 10 : 
            print(str(n % h) + '0' + str(n // h + 1) )
        else :
            print(str(n % h) + str(n // h + 1) )
 