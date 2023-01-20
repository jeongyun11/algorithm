def self_num():
    n = 1
    set_nonSelnum = set()

    while True :

        n_strsum = 0
        for num_str in str(n): # 각 자리수 더하기
            n_strsum += int(num_str)

        sum = n_strsum + n # n으로 selnum 완성
        if n > 10000 :
            break
        
        set_nonSelnum.add(sum) # selnum에 추가
        n += 1
        
    for i in range(1, 10001) :
        if i not in set_nonSelnum :
            print(i)

    return None

self_num()