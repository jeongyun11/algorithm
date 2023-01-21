N = int(input())

if N < 100 :
    cnt = N
else : 
    cnt = 99
    for i in range(100,N + 1) : # 100~1000 순환
        dict_ = {}
        for j in range(len(str(i)) - 1) : # 각 자리를 더해서
            dict_[int(str(i)[j]) - int(str(i)[j + 1])] =  dict_.get(int(str(i)[j]) - int(str(i)[j + 1]), 0) + 1

        if len(dict_) == 1 :
            cnt += 1
print(cnt)
