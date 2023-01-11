A, B = map(int,input().split())

if ((A == 2) and (B == 1)) or ((A == 3) and (B == 2)) or ((A == 1) and (B == 3)) : # 2 1, 3 2, 1 3
    print('A')
else : # 1 2, 2 3, 3 1
    print('B')