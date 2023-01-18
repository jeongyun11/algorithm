taebo = input()
# cnt = 0
# for i in taebo :
#     if i == '@' :
#         cnt +=1
#     elif i == '0' :
#         print(cnt,end = ' ')
#         cnt = 0
# print(cnt)

# 인덱스로 위치받고 슬라이스로 카운트
mouse = taebo.index('0')
print(taebo[:mouse].count('@'), taebo[mouse:].count('@'))