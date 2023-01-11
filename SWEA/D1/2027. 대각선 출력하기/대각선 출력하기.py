# 2027. 대각선 출력하기
# for i in range(5) :
#     for j in range(5) : 
#         if j == i : 
#             print('#', end='')
#         else : 
#             print('+', end='')
#     print()

for i in range(5) :
    print('+'*i, '#', '+'*(4-i), sep='')