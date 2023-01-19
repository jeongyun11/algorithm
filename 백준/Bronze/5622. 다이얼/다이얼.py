word = input()
len_apb = 3
fn_bef = 65
result = 0
for apb in word : # i는 전화기 번호, j는 각 전화기 번호의 아스키코드
    for i in range(2,9 + 1) : # 65 A 90 Z

        if (i == 7) or (i == 9) :
            len_apb = 4
        if (i == 8) :
            len_apb = 3

        # print (i) # test
        for j in range(fn_bef, fn_bef + len_apb) :
            # print (j,end=' ') # test
            if ord(apb) == j :
                result += i
            # print(result) # test
        fn_bef += len_apb
        # print() # test
    fn_bef = 65
    len_apb = 3
print(result + len(word))