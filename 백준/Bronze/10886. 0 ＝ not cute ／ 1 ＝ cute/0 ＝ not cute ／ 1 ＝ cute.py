# 10886
N = int(input())
cnt = 0
for n in range(N) :
    isCute = int(input())
    cnt += isCute

if (N / 2) < cnt :
    print('Junhee is cute!')
else :
    print('Junhee is not cute!')